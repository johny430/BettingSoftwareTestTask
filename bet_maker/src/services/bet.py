from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from src.caching.client import RedisClient
from src.enums.bet import BetStatus
from src.repository.bet import BetRepository
from src.schemas.bet import BetResponse

from src.repository.event import EventRepository


class BetService:

    def __init__(self, session: AsyncSession, client: RedisClient):
        self.bet_repository = BetRepository(session)
        self.event_repository = EventRepository(client)

    async def get_all_bets(self) -> Sequence[BetResponse]:
        return await self.bet_repository.get_all_bets()

    async def create_bet(self, bet) -> int | None:
        if not await self.event_repository.get_by_id(bet.event_id):
            return None
        return await self.bet_repository.create_bet(bet)

    async def update_status_by_event_id(self, event_id: int, status: BetStatus) -> bool:
        return await self.bet_repository.update_bets_status_by_event_id(event_id, status)
