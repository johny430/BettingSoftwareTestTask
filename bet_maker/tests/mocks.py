from src.enums.bet import BetStatus


class DummyBet:
    def __init__(self, event_id: int, sum: float):
        self.event_id = event_id
        self.sum = sum


DUMMY_BETS = [
    {
        "id": 1,
        "sum": 100,
        "event_id": 10,
        "created_at": "2025-04-07T00:00:00"
    }
]

DUMMY_STATUS = BetStatus.PENDING
