from caching.client import RedisClient
from repository.event import EventRepository


class EventService:

    def __init__(self, client: RedisClient):
        self.repository = EventRepository(client)

    async def get_all(self):
        return self.repository.get_all()
