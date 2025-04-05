from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from src.database.dependencies import setup_database
from src.database.models.base import mapper_registry
from src.messaging.dependecies import setup_rabbitmq


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    await setup_database(app)
    await setup_rabbitmq(app)
    async with app.state.db_engine.begin() as conn:
        await conn.run_sync(mapper_registry.metadata.create_all)

    yield

    await app.state.db_engine.dispose()
    await app.state.publisher.close()
