import logging
from typing import Sequence

from aiormq.tools import awaitable
from sqlalchemy import select
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

    async def update_bet_status(self, bet_id: int, state: BetState):
        query = select(Bet).where(Bet.id == bet_id)
        result = await self.session.execute(query)
        bet = result.scalar_one_or_none()
        if not bet:
            return
        bet.state = state
        self.session.add(bet)
        await self.session.commit()
