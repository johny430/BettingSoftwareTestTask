import aioredis

from caching.settings import redis_settings


class RedisClient:
    def __init__(self):
        self.redis = None

    async def connect(self):
        self.redis = await aioredis.from_url(redis_settings.redis_url, decode_responses=True)

    async def get(self, key: str):
        return await self.redis.get(key)

    async def set(self, key: str, value: str, expire: int = None):
        return await self.redis.setex(key, vakue=value, ex=expire)
