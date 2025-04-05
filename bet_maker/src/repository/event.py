from datetime import datetime

from caching.client import RedisClient
from caching.settings import redis_settings
from schemas.event import EventResponse, EventSchema


class EventRepository:

    def __init__(self, client: RedisClient):
        self.client = client

    async def get_all(self):
        events = await self.client.get_by_prefix(redis_settings.event_cache_key)
        a = [EventResponse(**event) for event in events]
        return a

    async def add_event(self, event: EventSchema):
        key = f"{redis_settings.event_cache_key}:{event.id}"
        ttl = int(event.deadline - datetime.now().timestamp())
        if ttl < 0:
            return
        await self.client.set(key, event.model_dump_json(), ttl)
