from decimal import Decimal

from pydantic import BaseModel

from src.enums.event import EventStatus


class Event(BaseModel):
    id: int
    coefficient: Decimal
    deadline: int
    status: EventStatus
