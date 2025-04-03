import logging
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from database.models.bet import Bet
from repository.base import BaseRepository
from schemas.bet import BetCreate

logger = logging.getLogger(__name__)


class BetRepository(BaseRepository):

    async def get_all_bets(self) -> Sequence[Bet]:
        query = select(Bet).order_by(Bet.created_at.desc())
        result = await self.session.execute(query)
        return result.scalars().all()

    async def create_bet(self, bet: BetCreate) -> int | None:
        new_bet = Bet(sum=bet.sum, event_id=bet.event_id)
        self.session.add(new_bet)
        try:
            await self.session.commit()
            return new_bet.id
        except IntegrityError:
            logger.error("Error in BetGateway")
        return None
