from src.caching.client import RedisClient
from src.repository.event import EventRepository
from src.schemas.event import EventSchema


class EventService:

    def __init__(self, client: RedisClient):
        self.repository = EventRepository(client)

    async def get_all(self):
        return await self.repository.get_all()

    async def add_event(self, event: EventSchema):
        return await self.repository.add_event(event)
