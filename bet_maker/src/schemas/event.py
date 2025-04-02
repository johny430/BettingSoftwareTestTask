from decimal import Decimal

from bet_maker.src.database.models.base import BaseModel
from bet_maker.src.enums.event import EventState


class Event(BaseModel):
    event_id: str
    coefficient: Decimal | None
    deadline: int | None
    state: EventState | None
