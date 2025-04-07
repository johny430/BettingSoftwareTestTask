from decimal import Decimal

from pydantic import BaseModel

from src.enums.event import EventState


class EventResponse(BaseModel):
    id: int
    coefficient: Decimal
    deadline: int | None
    state: EventState | None
