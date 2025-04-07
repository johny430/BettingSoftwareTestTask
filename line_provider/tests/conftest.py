from unittest.mock import AsyncMock

import pytest

from src.services.event import EventService
from tests.mocks import DUMMY_EVENT, DUMMY_EVENT_CREATE


@pytest.fixture
def event_repository_mock():
    repo = AsyncMock()
    repo.create.return_value = DUMMY_EVENT
    repo.get_by_id.return_value = DUMMY_EVENT
    repo.get_all.return_value = [DUMMY_EVENT]
    repo.update_status.return_value = DUMMY_EVENT
    return repo


@pytest.fixture
def event_sender_repository_mock():
    repo = AsyncMock()
    # Simulate methods that don't return a value.
    repo.send_event_created_message.return_value = None
    repo.send_event_status_updated_message.return_value = None
    return repo


@pytest.fixture
def event_service(event_repository_mock, event_sender_repository_mock):
    return EventService(
        event_repository=event_repository_mock,
        event_sender_repository=event_sender_repository_mock
    )


@pytest.fixture
def dummy_event_create():
    return DUMMY_EVENT_CREATE
