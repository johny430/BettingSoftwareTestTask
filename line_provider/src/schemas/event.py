from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, condecimal

from src.enums.event import EventStatus


class EventCreate(BaseModel):
    coefficient: condecimal(max_digits=10, decimal_places=2, gt=0)
    deadline: datetime
    status: EventStatus = EventStatus.NEW


class EventResponse(BaseModel):
    id: int
    coefficient: Decimal
    deadline: int | None
    status: EventStatus | None = EventStatus.NEW
