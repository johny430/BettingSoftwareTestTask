from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from bet_maker.src.repository.bet import BetRepository
from bet_maker.src.schemas.bet import Bet


class BetService:
    repository = BetRepository

    @classmethod
    async def get_all_bets(cls, session: AsyncSession) -> Sequence[Bet]:
        all_bets = await  cls.repository.get_all_bets(session)
        return [
            Bet(id=bet.id, state=bet.state, sum=bet.sum, event_id=bet.event_id)
            for bet in all_bets
        ]
