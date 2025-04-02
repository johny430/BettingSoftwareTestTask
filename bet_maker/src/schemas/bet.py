from decimal import Decimal

from pydantic import BaseModel

from bet_maker.src.enums.bet import BetState


class Bet(BaseModel):
    id: int | None
    state: BetState
    sum: Decimal
    event_id: str

    def update_state(self, state: BetState):
        self.state = state


class BetCreate(BaseModel):
    bet_sum: condecimal(max_digits=10, decimal_places=2)  # type: ignore
    event_id: str


class BetCreated(BaseModel):
    id: int
