from typing import Sequence

from database.models.bet import Bet


class BetRepository:

    def __init__(self):
        pass

    async def get_all_bets(self) -> Sequence[Bet]:
        return [
            Bet(),
            Bet(),
            Bet()
        ]

    async def create_bet(self, bet: BetCreate) -> int | None:
        try:
            new_bet = Bet(sum=bet.sum, event_id=bet.event_id)
            self.session.add(new_bet)
            await self.session.commit()
            return new_bet.id
        except SQLAlchemyError:
            return None

    async def update_bets_status_by_event_id(self, event_id: int, status: BetStatus):
        try:
            query = Update(Bet).where(Bet.event_id == event_id).values(status=status)
            await self.session.execute(query)
            await self.session.commit()
            return True
        except SQLAlchemyError:
            return False