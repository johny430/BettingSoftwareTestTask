from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, condecimal, field_validator

from src.enums.event import EventStatus


class EventCreate(BaseModel):
    coefficient: condecimal(max_digits=10, decimal_places=2, gt=0)
    deadline: int | datetime

    @field_validator('deadline')
    def timestamp_to_datetime(cls, timestamp):
        try:
            return datetime.fromtimestamp(timestamp).replace(tzinfo=None)
        except (OSError, OverflowError, ValueError):
            raise ValueError


class EventResponse(BaseModel):
    id: int
    coefficient: Decimal
    deadline: int | None
    status: EventStatus | None = EventStatus.NEW
