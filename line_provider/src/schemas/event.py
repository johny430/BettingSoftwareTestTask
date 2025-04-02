from decimal import Decimal

from pydantic import BaseModel
from enums.event import EventState


class Event(BaseModel):
    event_id: str
    coefficient: Decimal | None
    deadline: int | None
    state: EventState | None
