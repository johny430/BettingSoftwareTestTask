from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from database.factory import _setup_db
from database.models.base import mapper_registry


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    await _setup_db(app)
    async with app.state.db_engine.begin() as conn:
        await conn.run_sync(mapper_registry.metadata.create_all)

    yield

    await app.state.db_engine.dispose()
