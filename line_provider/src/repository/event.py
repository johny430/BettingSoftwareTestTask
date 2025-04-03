import logging
from typing import Sequence

from sqlalchemy import select

from repository.base import BaseRepository
from src.database.models.event import Event
from src.enums.event import EventState

logger = logging.getLogger(__name__)


class EventRepository(BaseRepository):

    async def create(self, event: Event) -> Event:
        self.session.add(event)
        await self.session.commit()
        await self.session.refresh(event)
        return event

    async def get_by_id(self, event_id: int) -> Event | None:
        query = select(Event).where(Event.id == event_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_all(self) -> Sequence[Event]:
        stmt = select(Event)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def update_status(self, event_id: int, new_status: EventState) -> Event | None:
        stmt = select(Event).where(Event.id == event_id)
        result = await self.session.execute(stmt)
        event = result.scalar_one_or_none()
        if event is None:
            return None
        event.state = new_status
        self.session.add(event)
        await self.session.commit()
        await self.session.refresh(event)
        return event
