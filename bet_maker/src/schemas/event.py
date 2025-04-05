from decimal import Decimal

from pydantic import BaseModel

from enums.event import EventState


class EventSchema(BaseModel):
    id: int
    coefficient: Decimal
    deadline: int | None
    state: EventState | None


class EventResponse(BaseModel):
    coefficient: Decimal
    deadline: int | None
    state: EventState | None
