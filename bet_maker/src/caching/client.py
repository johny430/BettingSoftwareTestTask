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
        if not keys:
            return []
        return [value for value in map(safe_json_loads, await self.redis.mget(*keys)) if value is not None]

    async def get(self, key):
        return safe_json_loads(await self.redis.get(key))

    async def set(self, key: str, value: str, ttl: int):
        return await self.redis.setex(key, ttl, value)
