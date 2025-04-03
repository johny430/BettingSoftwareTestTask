from dataclasses import Field
from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, field_validator, condecimal

from enums.event import EventState


class EventCreate(BaseModel):
    coefficient: condecimal(max_digits=10, decimal_places=2, gt=0)
    deadline: datetime

class EventResponse(BaseModel):
    id: int
    coefficient: Decimal
    deadline: int | None
    state: EventState | None


class EventUpdateStatus(BaseModel):
    state: EventState
