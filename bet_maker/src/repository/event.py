import json

from caching.client import RedisClient


class EventRepository:

    def __init__(self, client: RedisClient):
        self.client = client

    async def get_all(self):
        return await self.client.get("cached_events")

    async def add_event(self, event):
        await self.client.set("cached_events", json.dumps(event))
