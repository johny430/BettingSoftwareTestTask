from typing import Sequence

from src.database.models.event import Event
from src.enums.event import EventStatus
from src.repository.event import EventRepository
from src.repository.event_sender import EventSenderRepository
from src.schemas.event import EventCreate


class EventService:

    def __init__(self, event_repository: EventRepository, event_sender_repository: EventSenderRepository):
        self.event_repository = event_repository
        self.event_sender_repository = event_sender_repository

    async def create_event(self, event_data: EventCreate) -> Event | None:
        created_event = await self.event_repository.create(
            Event(deadline=event_data.deadline.replace(tzinfo=None), coefficient=event_data.coefficient)
        )
        await self.event_sender_repository.send_event_created_message(created_event)
        return created_event

    async def get_event_by_id(self, event_id: int) -> Event | None:
        return await self.event_repository.get_by_id(event_id)

    async def get_all_events(self) -> Sequence[Event]:
        return await self.event_repository.get_all()

    async def update_event_status(self, event_id: int, new_status: EventStatus) -> Event | None:
        updated_event = await self.event_repository.update_status(event_id, new_status)
        if updated_event:
            await self.event_sender_repository.send_event_status_updated_message(updated_event)
        return updated_event
