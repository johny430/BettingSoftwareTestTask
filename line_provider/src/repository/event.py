import logging
from typing import Sequence

from sqlalchemy import select, Update
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models.event import Event as EventORM
from src.schemas.event import EventCreate, Event, EventStatusUpdate


class EventRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, event: EventCreate) -> Event | None:
        try:
            new_event = EventORM(coefficient=event.coefficient, deadline=event.deadline)
            logging.getLogger(__name__).error(new_event)
            self.session.add(new_event)
            await self.session.commit()
            await self.session.refresh(new_event)
            return Event.model_validate(new_event)
        except SQLAlchemyError:
            return None

    async def get_by_id(self, event_id: int) -> Event | None:
        result = (await self.session.execute(select(EventORM).where(EventORM.id == event_id))).scalar_one_or_none()
        return Event.model_validate(result) if result else None

    async def get_all(self) -> Sequence[Event]:
        result = await self.session.execute(select(EventORM))
        return [Event.model_validate(value) for value in result.scalars().all()]

    async def update_status(self, event_status_update: EventStatusUpdate) -> Event | None:
        try:
            query = Update(EventORM).where(
                EventORM.id == event_status_update.id
            ).values(
                status=event_status_update.status
            )
            await self.session.execute(query)
            await self.session.commit()
            return await self.get_by_id(event_status_update.id)
        except SQLAlchemyError:
            return None
