from datetime import datetime
from unittest.mock import AsyncMock

import pytest
from src.services.bet import BetService

from src.enums.event import EventStatus
from src.schemas.event import Event
from tests.mocks import DUMMY_BETS, DummyBet


@pytest.fixture
def bet_repository_mock():
    repo = AsyncMock()
    repo.get_all_bets.return_value = DUMMY_BETS
    repo.create_bet.return_value = 1
    repo.update_bets_status_by_event_id.return_value = True
    return repo


@pytest.fixture
def event_repository_mock():
    repo = AsyncMock()
    repo.get_by_id.return_value = Event(
        id=10,
        coefficient=2,
        deadline=(int(datetime.now().timestamp() + 120)),
        status=EventStatus.NEW
    )
    repo.get_all.return_value = [Event(
        id=14,
        coefficient=23,
        deadline=(int(datetime.now().timestamp() + 134)),
        status=EventStatus.NEW
    )]
    return repo


@pytest.fixture
def bet_service(bet_repository_mock, event_repository_mock):
    return BetService(bet_repository=bet_repository_mock, event_repository=event_repository_mock)


@pytest.fixture
def dummy_bet():
    return DummyBet(event_id=999, sum=50)
