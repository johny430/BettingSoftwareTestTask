from src.repository.event import EventRepository
from src.schemas.event import EventStatus


class EventService:

    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    async def get_all(self):
        return await self.event_repository.get_all()

    async def add_event(self, event: EventStatus):
        return await self.event_repository.add_event(event)
