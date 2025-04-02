from decimal import Decimal
from enum import Enum

from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ENUM as PGENUM

from bet_maker.src.database.models.base import TimedBaseModel
from bet_maker.src.enums.bet import BetState


class BetStatus(Enum):
    NOT_PLAY = "Ещё не сыграла"
    WON = "Выиграла"
    LOST = "Проиграла"


class Bet(TimedBaseModel):
    __tablename__ = "bets"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    state: Mapped[BetState] = mapped_column(default=BetState.PENDING)
    sum: Mapped[Decimal]
    event_id: Mapped[str]