from decimal import Decimal

from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import TimedBaseModel
from src.enums.bet import BetState


class Bet(TimedBaseModel):
    __tablename__ = "bets"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    state: Mapped[BetState] = mapped_column(default=BetState.PENDING)
    sum: Mapped[Decimal]
    event_id: Mapped[int]
