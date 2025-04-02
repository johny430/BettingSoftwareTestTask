import logging
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from bet_maker.src.database.models.bet import Bet
from bet_maker.src.schemas.bet import BetCreate

logger = logging.getLogger(__name__)


class BetRepository:
    @classmethod
    async def get_all_bets(cls, session: AsyncSession) -> Sequence[Bet]:
        query = select(Bet).order_by(Bet.created_at)
        result = await session.execute(query)
        return result.scalars().all()

    @classmethod
    async def create_bet(cls, session: AsyncSession, bet: BetCreate) -> int | None:
        new_bet = Bet(sum=bet.sum, event_id=bet.event_id)
        session.add(new_bet)
        try:
            await session.commit()
            return new_bet.id
        except IntegrityError:
            logger.error("Error in BetGateway")
        return None
