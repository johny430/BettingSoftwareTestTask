import asyncio
import json
from contextlib import asynccontextmanager

import aio_pika
import uvicorn
from fastapi import FastAPI, Depends, HTTPException, APIRouter, Request
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.future import select
from sqlalchemy.orm import declarative_base


#########################################
# Database Setup (Stored in App State)
#########################################

def create_db_state():
    DATABASE_URL = "sqlite+aiosqlite:///./test.db"  # Using SQLite with async
    engine = create_async_engine(DATABASE_URL, echo=True, future=True)
    session_maker = async_sessionmaker(
        bind=engine,
        expire_on_commit=False,
        class_=AsyncSession
    )
    # Return a dictionary representing the database state
    # return {"db_engine": engine, "db_sessionmaker": session_maker}
    return engine, session_maker


@asynccontextmanager
async def lifespan(app: FastAPI):
    # On startup, create and store the db state in the app's state
    app.state.engine, app.state.session_maker = create_db_state()
    yield
    # On shutdown, dispose of the engine
    await app.state.engine.dispose()


# Dependency: yields an async database session from the request's app state.
async def get_db(request: Request):
    async with request.app.state.session_maker() as session:
        try:
            yield session
        except Exception:
            await session.rollback()


#########################################
# Domain Model
#########################################

Base = declarative_base()


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)


#########################################
# Repository Layer
#########################################

class ItemRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self):
        result = await self.session.execute(select(Item))
        return result.scalars().all()

    async def get_by_id(self, item_id: int):
        result = await self.session.execute(select(Item).where(Item.id == item_id))
        return result.scalars().first()

    async def create(self, name: str, description: str = None) -> Item:
        new_item = Item(name=name, description=description)
        self.session.add(new_item)
        await self.session.commit()
        await self.session.refresh(new_item)
        return new_item


#########################################
# Service Layer
#########################################

class ItemService:
    def __init__(self, repository: ItemRepository):
        self.repository = repository

    async def list_items(self):
        return await self.repository.get_all()

    async def get_item(self, item_id: int):
        item = await self.repository.get_by_id(item_id)
        if not item:
            raise Exception("Item not found")
        return item

    async def create_item(self, name: str, description: str = None):
        return await self.repository.create(name, description)


#########################################
# Routes
#########################################

router = APIRouter()


# Dependency that creates an ItemService using the injected DB session.
def get_item_service(db: AsyncSession = Depends(get_db)):
    repository = ItemRepository(db)
    return ItemService(repository)


@router.get("/")
async def read_items(service: ItemService = Depends(get_item_service)):
    raise HTTPException(status_code=500, detail="asd")
    try:
        items = await service.list_items()
        return items
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/")
async def create_item(name: str, description: str = None, service: ItemService = Depends(get_item_service)):
    try:
        item = await service.create_item(name, description)
        return item
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


#########################################
# FastAPI Application
#########################################

def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan, docs_url="/api/docs")
    app.include_router(router, prefix="/items", tags=["Items"])
    return app


#########################################
# RabbitMQ Consumer
#########################################

async def on_message(message: aio_pika.IncomingMessage):
    async with message.process():
        try:
            data = json.loads(message.body.decode())
            name = data.get("name")
            description = data.get("description")
            if not name:
                print("Message missing 'name'; skipping.")
                return

            # Instead of using a global, create a local db state for the consumer.
            db_state = create_db_state()
            async with db_state["db_sessionmaker"]() as session:
                repository = ItemRepository(session)
                service = ItemService(repository)
                item = await service.create_item(name, description)
                print(f"Item created successfully: {item.name}")
            await db_state["db_engine"].dispose()
        except Exception as e:
            print(f"Error processing message: {e}")


async def run_consumer():
    # Connect to RabbitMQ (update URL as needed)
    connection = await aio_pika.connect_robust("amqp://guest:guest@localhost/")
    channel = await connection.channel()
    # Declare a durable queue named 'item_queue'
    queue = await channel.declare_queue("item_queue", durable=True)
    # Start consuming messages
    await queue.consume(on_message)
    print(" [*] Waiting for messages. To exit press CTRL+C")
    # Run indefinitely.
    await asyncio.Future()


#########################################
# Main Entrypoint
#########################################

if __name__ == '__main__':
    app = create_app()
    # Run the FastAPI application using Uvicorn.
    uvicorn.run(app, host="127.0.0.1", port=8000)
