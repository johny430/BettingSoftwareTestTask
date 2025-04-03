from datetime import datetime
from decimal import Decimal

from sqlalchemy import Numeric, DateTime, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from database.models.base import TimedBaseModel
from enums.event import EventState


class Event(TimedBaseModel):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    coefficient: Mapped[Decimal] = mapped_column(Numeric(precision=10, scale=2), nullable=False)
    deadline: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    state: Mapped[EventState] = mapped_column(default=EventState.NEW)

    __table_args__ = (
        CheckConstraint("coefficient > 0", name="ck_coefficient_positive"),
    )
