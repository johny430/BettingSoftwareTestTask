from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from repository.bet import BetRepository
from schemas.bet import Bet
from services.base import BaseService


class BetService(BaseService):

    def __init__(self, session: AsyncSession):
        super().__init__(BetRepository, session)

    async def get_all_bets(self) -> Sequence[Bet]:
        all_bets = await self.repository.get_all_bets()
        return [
            Bet(id=bet.id, state=bet.state, sum=bet.sum, event_id=bet.event_id)
            for bet in all_bets
        ]

    async def create_bet(self, created_bet) -> int | None:
        return await self.repository.create_bet(created_bet)
