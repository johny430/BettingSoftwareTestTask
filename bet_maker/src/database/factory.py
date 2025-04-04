from fastapi import FastAPI
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine, AsyncSession,
)

from database.models.base import mapper_registry
from src.database.settings import postgres_settings


def create_db_state():
    engine = create_async_engine(str(postgres_settings.db_url), echo=True, future=True)
    session_maker = async_sessionmaker(
        bind=engine,
        expire_on_commit=False,
        class_=AsyncSession
    )
    return engine, session_maker


async def setup_database(app: FastAPI):
    app.state.db_engine, app.state.session_maker = create_db_state()

    async with app.state.db_engine.begin() as conn:
        await conn.run_sync(mapper_registry.metadata.create_all)


async def close_database_connection(app: FastAPI):
    await app.state.db_engine.dispose()
