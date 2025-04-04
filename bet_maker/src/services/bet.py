from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from bet_maker.src.repository.bet import BetRepository
from schemas.bet import BetResponse


class BetService:

    def __init__(self, session: AsyncSession):
        self.repository = BetRepository(session)

    async def get_all_bets(self) -> Sequence[BetResponse]:
        all_bets = await self.repository.get_all_bets()
        return [
            BetResponse(id=bet.id, state=bet.state, sum=bet.sum, event_id=bet.event_id)
            for bet in all_bets
        ]

    async def create_bet(self, created_bet) -> int | None:
        return await self.repository.create_bet(created_bet)
