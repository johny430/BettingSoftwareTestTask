from typing import Any, Sequence

from src.database.models.event import Event
from src.enums.event import EventState
from src.repository.event import EventRepository
from src.schemas.event import EventCreate


class EventService:
    def __init__(self, repository: EventRepository):
        self.repository = repository

    async def create_event(self, event_data: EventCreate) -> Event:
        event = Event(
            coefficient=event_data.coefficient,
            deadline=event_data.deadline,
            state=event_data.state
        )
        return await self.repository.create(event)

    async def get_event_by_id(self, event_id: int) -> Event | None:
        return await self.repository.get_by_id(event_id)

    async def get_all_events(self) -> Sequence[Any]:
        return await self.repository.get_all()

    async def update_event_status(self, event_id: int, new_status: EventState) -> Event | None:
        return await self.repository.update_status(event_id, new_status)
