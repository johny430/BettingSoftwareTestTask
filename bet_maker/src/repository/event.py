from datetime import datetime

from src.caching.client import RedisClient
from src.caching.settings import redis_settings
from src.schemas.event import EventResponse, EventSchema


class EventRepository:

    def __init__(self, client: RedisClient):
        self.client = client

    async def get_all(self):
        return [EventResponse(**event) for event in await self.client.get_by_prefix(redis_settings.event_cache_key)]

    async def add_event(self, event: EventSchema):
        key = f"{redis_settings.event_cache_key}:{event.id}"
        ttl = int(event.deadline - datetime.now().timestamp())
        if ttl < 0:
            return
        await self.client.set(key, event.model_dump_json(), ttl)

    async def get_by_id(self, event_id: int):
        return await self.client.get(f"{redis_settings.event_cache_key}:{event_id}")
