from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.app import settings
from src.database.settings import postgres_settings
from src.messaging.client import RabbitMQPublisher


async def setup_db(app: FastAPI) -> None:
    engine = create_async_engine(str(postgres_settings.db_url))
    session_factory = async_sessionmaker(
        engine,
        expire_on_commit=False,
    )
    app.state.db_engine = engine
    app.state.db_session_factory = session_factory

async def setup_rabbitmq(app: FastAPI) -> None:
    app.state.publisher = RabbitMQPublisher()
    await app.state.publisher.connect()