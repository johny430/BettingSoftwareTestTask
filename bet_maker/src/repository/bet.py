from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from bet_maker.src.database.models.bet import Bet


class BetRepository:
    @classmethod
    async def get_all_bets(cls, session: AsyncSession) -> Sequence[Bet]:
        query = select(Bet).order_by(Bet.created_at)
        result = await session.execute(query)
        return result.scalars().all()
