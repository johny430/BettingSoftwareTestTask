from fastapi import FastAPI
from sqlalchemy import AsyncAdaptedQueuePool
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.database.settings import postgres_settings


async def setup_db(app: FastAPI) -> None:
    engine = create_async_engine(str(postgres_settings.postgresql_settings.db_url))
    session_factory = async_sessionmaker(
        engine,
        expire_on_commit=False,
    )
    app.state.db_engine = engine
    app.state.db_session_factory = session_factory


def create_session_maker(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    pool: async_sessionmaker[AsyncSession] = async_sessionmaker(
        bind=engine, expire_on_commit=False
    )
    return pool


def create_engine(database_url: str) -> AsyncEngine:
    return create_async_engine(
        url=database_url,
        poolclass=AsyncAdaptedQueuePool,
        pool_size=3,
        max_overflow=2
    )
