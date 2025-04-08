from datetime import datetime
from decimal import Decimal

from fastapi import Path, Query
from pydantic import BaseModel, condecimal, field_validator, ConfigDict

from src.enums.event import EventStatus


class Event(BaseModel):
    id: int
    coefficient: Decimal
    deadline: datetime
    status: EventStatus

    model_config = ConfigDict(
        from_attributes=True,
        json_encoders={
            datetime: lambda v: int(v.timestamp())
        }
    )


class EventCreate(BaseModel):
    coefficient: condecimal(max_digits=10, decimal_places=2, gt=0)
    deadline: int | datetime

    @field_validator('deadline')
    def timestamp_to_datetime(cls, v):
        try:
            return (v if isinstance(v, datetime) else datetime.fromtimestamp(v)).replace(tzinfo=None)
        except (OSError, OverflowError, ValueError):
            raise ValueError


class EventStatusUpdate(BaseModel):
    id: int
    status: EventStatus

    @classmethod
    def as_dependency(cls, event_id: int = Path(...), status: EventStatus = Query(...)) -> "EventStatusUpdate":
        return cls(id=event_id, status=status)


class EventResponse(BaseModel):
    coefficient: Decimal
    deadline: datetime
    status: EventStatus
