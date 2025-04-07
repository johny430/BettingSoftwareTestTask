from decimal import Decimal
from unittest.mock import AsyncMock

import pytest
from src.schemas.bet import BetCreate, BetResponse

from src.schemas.event import EventSchema

@pytest.fixture
def mock_bet_service() -> AsyncMock:
    """Returns an AsyncMock instance for BetService."""
    return AsyncMock()


@pytest.fixture
def mock_event_service() -> AsyncMock:
    """Returns an AsyncMock instance for EventService."""
    return AsyncMock()

@pytest.fixture
def sample_bet() -> BetCreate:
    """A sample bet creation request."""
    return BetCreate(sum=Decimal("100.00"), event_id=1)


@pytest.fixture
def sample_bets() -> list[BetResponse]:
    """A list with a single sample bet response.
       Adjust 'PENDING' to match your BetState enum if needed."""
    return [BetResponse(id=1, state="PENDING", sum=Decimal("100.00"), event_id=1)]


@pytest.fixture
def sample_event() -> EventSchema:
    """A sample event schema instance."""
    return EventSchema(id=1, coefficient=Decimal("1.5"), deadline=None, state=None)
