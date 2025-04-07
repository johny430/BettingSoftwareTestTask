from datetime import datetime
from decimal import Decimal
from unittest.mock import AsyncMock

import pytest

from src.enums.event import EventState
from src.schemas.event import EventResponse, EventCreate


@pytest.fixture
def sample_event_create() -> EventCreate:
    return EventCreate(
        coefficient=Decimal("2.50"),
        deadline=datetime.now(),
        state=EventState.NEW
    )


@pytest.fixture
def sample_event_response() -> EventResponse:
    return EventResponse(
        id=1,
        coefficient=Decimal("2.50"),
        deadline=int(datetime.now().timestamp()),
        state=EventState.NEW
    )


@pytest.fixture
def mock_event_service() -> AsyncMock:
    return AsyncMock()
