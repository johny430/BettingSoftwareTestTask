from typing import Sequence

from sqlalchemy import select, Update
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.models.bet import Bet
from src.enums.bet import BetStatus
from src.schemas.bet import BetCreate


class BetRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_bets(self) -> Sequence[Bet]:
        query = select(Bet).order_by(Bet.created_at.desc())
        result = await self.session.execute(query)
        return result.scalars().all()

    async def create_bet(self, bet: BetCreate) -> int | None:
        try:
            new_bet = Bet(sum=bet.sum, event_id=bet.event_id)
            self.session.add(new_bet)
            await self.session.commit()
            return new_bet.id
        except SQLAlchemyError:
            return None

    async def update_bets_status_by_event_id(self, event_id: int, status: BetStatus):
        try:
            query = Update(Bet).where(Bet.event_id == event_id).values(status=status)
            await self.session.execute(query)
            await self.session.commit()
            return True
        except SQLAlchemyError:
            return False
