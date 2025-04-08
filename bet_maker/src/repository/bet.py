from typing import Sequence

from sqlalchemy import select, Update
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.models.bet import Bet as BetORM
from src.enums.bet import BetStatus
from src.schemas.bet import BetCreate, Bet


class BetRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_bets(self) -> Sequence[Bet]:
        result = await self.session.execute(select(BetORM).order_by(BetORM.created_at.desc()))
        return [Bet.model_validate(value) for value in result.scalars().all()]

    async def create_bet(self, bet: BetCreate) -> Bet | None:
        try:
            created_bet = BetORM(sum=bet.sum, event_id=bet.event_id)
            self.session.add(created_bet)
            await self.session.commit()
            await self.session.refresh(created_bet)
            return Bet.model_validate(created_bet)
        except SQLAlchemyError:
            return None

    async def get_by_id(self, event_id: int) -> Bet | None:
        result = (await self.session.execute(select(BetORM).where(BetORM.id == event_id))).scalar_one_or_none()
        return Bet.model_validate(result) if result else None

    async def update_bets_status_by_event_id(self, event_id: int, status: BetStatus) -> Bet:
        try:
            await self.session.execute(Update(BetORM).where(BetORM.event_id == event_id).values(status=status))
            await self.session.commit()
            return True
        except SQLAlchemyError:
            return False
