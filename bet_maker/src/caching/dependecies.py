from fastapi import FastAPI
from starlette.requests import Request

from caching.client import RedisClient


async def setup_redis(app: FastAPI) -> None:
    app.state.cache = RedisClient()
    await app.state.cache.connect()


async def get_redis_client(request: Request):
    yield request.app.state.cache