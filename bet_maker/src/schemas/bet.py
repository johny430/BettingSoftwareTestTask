from decimal import Decimal

from pydantic import BaseModel, condecimal

from src.enums.bet import BetStatus


class BetResponse(BaseModel):
    id: int | None
    state: BetStatus
    sum: Decimal
    event_id: int

    def update_state(self, state: BetStatus):
        self.state = state


class BetCreate(BaseModel):
    sum: condecimal(max_digits=10, decimal_places=2, gt=0)  # type: ignore
    event_id: int


class BetCreated(BaseModel):
    id: int
