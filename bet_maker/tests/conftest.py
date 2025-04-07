from decimal import Decimal
from typing import Sequence

import pytest
from src.enums.bet import BetStatus
from src.schemas.bet import BetCreate, BetResponse

from bet_maker.tests.mock import MockBetService
from src.schemas.event import EventResponse


@pytest.fixture
def mock_bet_service() -> MockBetService:
    return MockBetService()


@pytest.fixture
def sample_bet() -> BetCreate:
    return BetCreate(sum=Decimal("100.00"), event_id=1)


@pytest.fixture
def sample_bets() -> Sequence[BetResponse]:
    return [BetResponse(id=1, status=BetStatus.PENDING, sum=Decimal("100.00"), event_id=1)]


@pytest.fixture
def sample_event() -> EventResponse:
    return EventResponse(id=1, coefficient=Decimal("1.5"), deadline=None, state=None)
