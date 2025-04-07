from decimal import Decimal
from typing import Sequence

from enums.bet import BetStatus
from schemas.bet import BetResponse
from services.bet import BetService


class MockBetService(BetService):
    def __int__(self):
        pass

    async def get_all_bets(self) -> Sequence[BetResponse]:
        return [
            BetResponse(id=1, status=BetStatus.PENDING, sum=Decimal("100.00"), event_id=1),
            BetResponse(id=1, status=BetStatus.WIN, sum=Decimal("125.00"), event_id=2),
            BetResponse(id=1, status=BetStatus.LOSE, sum=Decimal("145.00"), event_id=3)
        ]

