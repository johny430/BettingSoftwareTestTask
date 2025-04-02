from sqlalchemy.ext.asyncio import AsyncSession

from bet_maker.src.repository.bet import BetRepository


class BetService:
    repository = BetRepository

    @classmethod
    async def get_all_bets(cls, session: AsyncSession):
        return cls.repository.get_all_bets(session)