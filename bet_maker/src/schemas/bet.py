from decimal import Decimal

from pydantic import BaseModel, condecimal
from src.enums.bet import BetStatus


class BetResponse(BaseModel):
    id: int | None
    status: BetStatus
    sum: Decimal
    event_id: int


class BetCreate(BaseModel):
    sum: condecimal(max_digits=10, decimal_places=2, gt=0)
    event_id: int


class BetCreated(BaseModel):
    id: int
