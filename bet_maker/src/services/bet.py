from typing import Sequence

from src.enums.bet import BetStatus
from src.repository.bet import BetRepository
from src.schemas.bet import Bet

from src.repository.event import EventRepository


class BetService:

    def __init__(self, bet_repository: BetRepository, event_repository: EventRepository):
        self.bet_repository = bet_repository
        self.event_repository = event_repository

    async def get_all_bets(self) -> Sequence[Bet]:
        return await self.bet_repository.get_all_bets()

    async def get_by_id(self, bet_id: int) -> Bet:
        return await self.bet_repository.get_by_id(bet_id)

    async def create_bet(self, bet) -> Bet | None:
        if not await self.event_repository.get_by_id(bet.event_id):
            return None
        return await self.bet_repository.create_bet(bet)

    async def update_status_by_event_id(self, event_id: int, status: BetStatus) -> bool:
        return await self.bet_repository.update_bets_status_by_event_id(event_id, status)
