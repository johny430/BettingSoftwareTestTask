from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from repository.bet import BetRepository
from caching.client import RedisClient
from database.models.bet import Bet
from enums.bet import BetState
from repository.event import EventRepository


class BetService:

    def __init__(self, session: AsyncSession, client: RedisClient):
        self.bet_repository = BetRepository(session)
        self.event_repository = EventRepository(client)

    async def get_all_bets(self) -> Sequence[Bet]:
        return await self.bet_repository.get_all_bets()

    async def create_bet(self, bet) -> int | None:
        if not await self.event_repository.get_by_id(bet.event_id):
            return None
        return await self.bet_repository.create_bet(bet)

    async def update_status_by_event_id(self, event_id: int, status: BetState):
        return await self.bet_repository.update_bets_status_by_event_id(event_id, status)
