from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models.event import Event
from src.enums.event import EventState
from src.repository.event import EventRepository
from src.schemas.event import EventCreate


class EventService:

    def __init__(self, session: AsyncSession, event_sender):
        self.event_sender = event_sender
        self.repository = EventRepository(session)

    async def create_event(self, event_data: EventCreate) -> Event | None:
        created_event = await self.repository.create(
            Event(deadline=event_data.deadline.replace(tzinfo=None), coefficient=event_data.coefficient)
        )
        await self.event_sender.send_event_created_message(created_event)
        return created_event

    async def get_event_by_id(self, event_id: int) -> Event | None:
        return await self.repository.get_by_id(event_id)

    async def get_all_events(self) -> Sequence[Event]:
        return await self.repository.get_all()

    async def update_event_status(self, event_id: int, new_status: EventState) -> Event | None:
        updated_event = await self.repository.update_status(event_id, new_status)
        await self.event_sender.send_event_created_message(updated_event)
        return updated_event
