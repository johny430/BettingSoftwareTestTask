from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from bet_maker.src.repository.bet import BetRepository
from database.models.bet import Bet
from schemas.bet import BetResponse


class BetService:

    def __init__(self, session: AsyncSession):
        self.repository = BetRepository(session)

    async def get_all_bets(self) -> Sequence[Bet]:
        return await self.repository.get_all_bets()

    async def create_bet(self, bet) -> int | None:
        return await self.repository.create_bet(bet)
