from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from repository.bet import BetRepository
from schemas.bet import Bet


class BetService:
    repository = BetRepository

    @classmethod
    async def get_all_bets(cls, session: AsyncSession) -> Sequence[Bet]:
        all_bets = await cls.repository.get_all_bets(session)
        return [
            Bet(id=bet.id, state=bet.state, sum=bet.sum, event_id=bet.event_id)
            for bet in all_bets
        ]

    @classmethod
    async def create_bet(cls, session: AsyncSession, created_bet) -> int | None:
        return await cls.repository.create_bet(session, created_bet)
