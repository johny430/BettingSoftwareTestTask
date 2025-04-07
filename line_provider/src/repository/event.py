from typing import Sequence

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models.event import Event
from src.enums.event import EventStatus
from src.schemas.event import EventCreate


class EventRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, event: EventCreate) -> Event | None:
        try:
            new_event = Event(coefficient=event.coefficient, deadline=event.deadline)
            self.session.add(new_event)
            await self.session.commit()
            await self.session.refresh(event)
            return new_event
        except SQLAlchemyError:
            return None

    async def get_by_id(self, event_id: int) -> Event | None:
        query = select(Event).where(Event.id == event_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_all(self) -> Sequence[Event]:
        query = select(Event)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def update_status(self, event_id: int, new_status: EventStatus) -> Event | None:
        event = await self.get_by_id(event_id)
        if event is None:
            return None
        event.status = new_status.name
        self.session.add(event)
        await self.session.commit()
        return event
