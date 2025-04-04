from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from caching.dependecies import setup_redis, close_redis_connection
from database.dependencies import setup_database, close_database_connection


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    await setup_database(app)
    await setup_redis(app)

    yield

    await close_database_connection(app)
    await close_redis_connection(app)
