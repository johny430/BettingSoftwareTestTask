import pytest

from src.enums.event import EventStatus
from tests.mocks import DUMMY_EVENT


@pytest.mark.asyncio
async def test_create_event(event_service, event_repository_mock, event_sender_repository_mock, dummy_event_create):
    result = await event_service.create_event(dummy_event_create)
    assert result == DUMMY_EVENT
    event_repository_mock.create.assert_awaited_once_with(dummy_event_create)
    event_sender_repository_mock.send_event_created_message.assert_awaited_once_with(DUMMY_EVENT)


@pytest.mark.asyncio
async def test_get_event_by_id(event_service, event_repository_mock):
    event_id = 1
    result = await event_service.get_event_by_id(event_id)
    assert result == DUMMY_EVENT
    event_repository_mock.get_by_id.assert_awaited_once_with(event_id)


@pytest.mark.asyncio
async def test_update_event_status_success(event_service, event_repository_mock, event_sender_repository_mock):
    event_id = 1
    new_status = EventStatus.FINISHED_WIN  # Ensure that COMPLETED exists in your EventStatus enum.
    result = await event_service.update_event_status(event_id, new_status)
    assert result == DUMMY_EVENT
    event_repository_mock.update_status.assert_awaited_once_with(event_id, new_status)
    event_sender_repository_mock.send_event_status_updated_message.assert_awaited_once_with(DUMMY_EVENT.id, new_status)
