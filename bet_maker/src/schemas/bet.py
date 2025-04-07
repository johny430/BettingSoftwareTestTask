from decimal import Decimal

from pydantic import BaseModel, condecimal, ConfigDict
from src.enums.bet import BetStatus


class Bet(BaseModel):
    id: int
    status: BetStatus
    sum: Decimal
    event_id: int

    model_config = ConfigDict(from_attributes=True)


class BetResponse(BaseModel):
    status: BetStatus
    sum: Decimal
    event_id: int


class BetCreate(BaseModel):
    sum: condecimal(max_digits=10, decimal_places=2, gt=0)
    event_id: int
