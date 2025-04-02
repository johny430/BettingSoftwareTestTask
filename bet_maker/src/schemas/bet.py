from decimal import Decimal
from enum import Enum
from pydantic import BaseModel, Field

class BetState(Enum):
    WIN = "WIN"
    LOSE = "LOSE"
    PENDING = "PENDING"


class Bet(BaseModel):
    id: int | None
    state: BetState
    sum: Decimal
    event_id: str

    def update_state(self, state: BetState):
        self.state = state