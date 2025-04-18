from fastapi import FastAPI
from starlette.requests import Request

from src.caching.client import RedisClient


async def setup_redis(app: FastAPI) -> None:
    app.state.cache = RedisClient()
    await app.state.cache.connect()


async def close_redis_connection(app: FastAPI):
    await app.state.cache.close()


async def get_redis_client(request: Request):
    yield request.app.state.cache
