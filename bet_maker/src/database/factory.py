from fastapi import FastAPI
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
)

from src.database.settings import postgres_settings


async def start_database_connection():
    engine = create_async_engine(str(postgres_settings.db_url))
    session_factory = async_sessionmaker(
        engine,
        expire_on_commit=False,
    )
    return engine, session_factory


async def setup_db(app: FastAPI) -> None:
    app.state.db_engine, app.state.db_session_factory = await start_database_connection()
