from datetime import datetime
from typing import Sequence

from src.caching.client import RedisClient

from src.app.settings import settings
from src.schemas.event import Event


class EventRepository:

    def __init__(self, client: RedisClient):
        self.client = client

    async def get_all(self) -> Sequence[Event]:
        return [
            Event(**event) for event in
            await self.client.get_by_prefix(settings.redis_settings.event_cache_key)
        ]

    async def add_event(self, event: Event) -> None:
        key = f"{settings.redis_settings.event_cache_key}:{event.id}"
        ttl = int(event.deadline - datetime.now().timestamp())
        if ttl < 0:
            return
        await self.client.set(key, event.model_dump_json(), ttl)

    async def get_by_id(self, event_id: int) -> Event | None:
        result = await self.client.get(f"{settings.redis_settings.event_cache_key}:{event_id}")
        return Event(**result) if result else None
