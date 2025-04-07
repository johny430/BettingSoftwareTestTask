import aioredis
from aioredis import Redis
from src.utils import safe_json_loads

from src.app.settings import settings


class RedisClient:
    def __init__(self):
        self.redis: Redis = None

    async def connect(self):
        self.redis = await aioredis.from_url(str(settings.redis_settings.redis_url), decode_responses=True)

    async def close(self):
        await self.redis.close()

    async def get_by_prefix(self, key_prefix: str):
        keys = await self.redis.keys(f"{key_prefix}*")
        return [
            value for value in map(safe_json_loads, await self.redis.mget(*keys)) if
            value is not None
        ] if keys else []

    async def get(self, key):
        result = await self.redis.get(key)
        return safe_json_loads(result) if result else None

    async def set(self, key: str, value: str, ttl: int):
        return await self.redis.setex(key, ttl, value)
