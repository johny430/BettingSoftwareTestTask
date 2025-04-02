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
