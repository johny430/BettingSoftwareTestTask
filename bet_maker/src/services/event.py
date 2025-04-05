from caching.client import RedisClient
from repository.event import EventRepository
from schemas.event import EventSchema


class EventService:

    def __init__(self, client: RedisClient):
        self.repository = EventRepository(client)

    async def get_all(self):
        return await self.repository.get_all()

    async def add_event(self, event: EventSchema):
        return await self.repository.add_event(event)
