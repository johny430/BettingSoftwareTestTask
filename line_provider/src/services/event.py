from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models.event import Event
from src.enums.event import EventState
from src.repository.event import EventRepository
from src.schemas.event import EventCreate, EventResponse
from src.services.base import BaseService


class EventService(BaseService):
    def __init__(self, session: AsyncSession):
        super().__init__(EventRepository, session)

    async def create_event(self, event_data: EventCreate) -> int | None:
        return await self.repository.create(
            Event(deadline=event_data.deadline.replace(tzinfo=None), coefficient=event_data.coefficient))

    async def get_event_by_id(self, event_id: int) -> Event | None:
        return await self.repository.get_by_id(event_id)

    async def get_all_events(self) -> Sequence[EventResponse]:
        return await self.repository.get_all()

    async def update_event_status(self, event_id: int, new_status: EventState) -> Event | None:
        return await self.repository.update_status(event_id, new_status)
