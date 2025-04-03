from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel

from enums.event import EventState


class EventCreate(BaseModel):
    coefficient: Decimal
    deadline: datetime
    state: EventState = EventState.NEW  # Optional, defaults to NEW


class EventResponse(BaseModel):
    event_id: str
    coefficient: Decimal | None
    deadline: int | None
    state: EventState | None


class EventUpdateStatus(BaseModel):
    state: EventState
