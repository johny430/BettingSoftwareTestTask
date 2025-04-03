import logging
from typing import Sequence

from database.models.event import Event
from sqlalchemy import select

from repository.base import BaseRepository

logger = logging.getLogger(__name__)


class BetRepository(BaseRepository):

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
