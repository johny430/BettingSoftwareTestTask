import pytest
from fastapi import HTTPException

from src.web.v1.line_router import create_event, get_event, get_events


@pytest.mark.asyncio
async def test_create_event_success(sample_event_create, sample_event_response, mock_event_service):
    mock_event_service.create_event.return_value = sample_event_response
    result = await create_event(sample_event_create, mock_event_service)
    assert result == sample_event_response
    mock_event_service.create_event.assert_awaited_once_with(sample_event_create)


@pytest.mark.asyncio
async def test_create_event_failure(sample_event_create, mock_event_service):
    mock_event_service.create_event.return_value = None
    with pytest.raises(HTTPException) as exc_info:
        await create_event(sample_event_create, mock_event_service)
    assert exc_info.value.status_code == 500
    assert exc_info.value.detail == "Error during event creation"


@pytest.mark.asyncio
async def test_get_event_success(sample_event_response, mock_event_service):
    mock_event_service.get_event_by_id.return_value = sample_event_response
    result = await get_event(1, mock_event_service)
    assert result == sample_event_response
    mock_event_service.get_event_by_id.assert_awaited_once_with(1)


@pytest.mark.asyncio
async def test_get_event_not_found(mock_event_service):
    mock_event_service.get_event_by_id.return_value = None
    with pytest.raises(HTTPException) as exc_info:
        await get_event(1, mock_event_service)
    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Event not found"


@pytest.mark.asyncio
async def test_get_all_events(sample_event_response, mock_event_service):
    mock_event_service.get_all_events.return_value = [sample_event_response]
    result = await get_events(mock_event_service)
    assert result == [sample_event_response]
    mock_event_service.get_all_events.assert_awaited_once()
