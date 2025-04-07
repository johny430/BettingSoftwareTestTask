from decimal import Decimal
from unittest.mock import AsyncMock

import pytest
from src.schemas.bet import BetCreate, BetResponse

from src.schemas.event import EventSchema


@pytest.fixture
def mock_bet_service() -> AsyncMock:
    return AsyncMock()


@pytest.fixture
def mock_event_service() -> AsyncMock:
    return AsyncMock()


@pytest.fixture
def sample_bet() -> BetCreate:
    return BetCreate(sum=Decimal("100.00"), event_id=1)


@pytest.fixture
def sample_bets() -> list[BetResponse]:
    return [BetResponse(id=1, state="PENDING", sum=Decimal("100.00"), event_id=1)]


@pytest.fixture
def sample_event() -> EventSchema:
    return EventSchema(id=1, coefficient=Decimal("1.5"), deadline=None, state=None)
