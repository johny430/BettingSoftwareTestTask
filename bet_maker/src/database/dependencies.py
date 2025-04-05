from typing import AsyncGenerator

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine, )
from starlette.requests import Request

from database.models.base import mapper_registry
from repository.bet import logger
from src.database.settings import postgres_settings


def create_database_connection():
    engine = create_async_engine(str(postgres_settings.db_url), future=True)
    session_maker = async_sessionmaker(
        bind=engine,
        expire_on_commit=False,
        class_=AsyncSession
    )
    return engine, session_maker


async def setup_database(app: FastAPI):
    app.state.db_engine, app.state.db_session_factory = create_database_connection()

    async with app.state.db_engine.begin() as conn:
        await conn.run_sync(mapper_registry.metadata.create_all)


async def close_database_connection(app: FastAPI):
    await app.state.db_engine.dispose()


async def get_db_session(request: Request) -> AsyncGenerator[AsyncSession, None]:
    async with request.app.state.db_session_factory() as session:
        try:
            yield session
        except Exception as e:
            logger.error(e)
            await session.rollback()
            raise
        finally:
            await session.commit()
            await session.close()
