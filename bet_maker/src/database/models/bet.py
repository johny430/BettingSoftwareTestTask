from decimal import Decimal

from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import TimedBaseModel
from src.enums.bet import BetStatus


class Bet(TimedBaseModel):
    __tablename__ = "bets"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    state: Mapped[BetStatus] = mapped_column(default=BetStatus.PENDING)
    sum: Mapped[Decimal]
    event_id: Mapped[int]
