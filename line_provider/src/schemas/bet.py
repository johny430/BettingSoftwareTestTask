from decimal import Decimal

from pydantic import BaseModel, condecimal

from enums.bet import BetState


class Bet(BaseModel):
    id: int | None
    state: BetState
    sum: Decimal
    event_id: int

    def update_state(self, state: BetState):
        self.state = state


class BetCreate(BaseModel):
    sum: condecimal(max_digits=10, decimal_places=2, gt=0)  # type: ignore
    event_id: int


class BetCreated(BaseModel):
    id: int
