from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from bet_maker.src.repository.bet import BetRepository
from caching.client import RedisClient
from database.models.bet import Bet
from repository.event import EventRepository
from schemas.bet import BetResponse


class BetService:

    def __init__(self, session: AsyncSession, client: RedisClient):
        self.bet_repository = BetRepository(session)
        self.event_repository = EventRepository(client)

    async def get_all_bets(self) -> Sequence[Bet]:
        return await self.bet_repository.get_all_bets()

    async def create_bet(self, bet) -> int | None:
        if not self.event_repository.get_by_id(bet.event_id):
            return None
        return await self.bet_repository.create_bet(bet)
