from decimal import Decimal

from pydantic import BaseModel

from src.enums.event import EventStatus


class EventResponse(BaseModel):
    id: int
    coefficient: Decimal
    deadline: int
    state: EventStatus


class EventCreate(EventResponse):
    pass
