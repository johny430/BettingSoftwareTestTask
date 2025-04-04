import aioredis
from aioredis import Redis

from caching.settings import redis_settings


class RedisClient:
    def __init__(self):
        self.redis: Redis = None

    async def connect(self):
        self.redis = await aioredis.from_url(str(redis_settings.redis_url), decode_responses=True)

    async def close(self):
        await self.redis.close()

    async def get(self, key: str):
        return await self.redis.get(key)

    async def set(self, key: str, value: str, expire: int = None):
        return await self.redis.setex(key, vakue=value, ex=expire)
