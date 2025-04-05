import logging
from typing import Sequence

from aiormq.tools import awaitable
from sqlalchemy import select, Update
from sqlalchemy.ext.asyncio import AsyncSession

from database.models.bet import Bet
from enums.bet import BetState
from schemas.bet import BetCreate

logger = logging.getLogger(__name__)


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
        except Exception as e:
            logger.error(e)
            return None

    async def update_bets_status_by_event_id(self, event_id: int, status: BetState):
        try:
            query = Update(Bet).where(Bet.event_id == event_id).values(state = status)
            await self.session.execute(query)
            return True
        except Exception:
            return False