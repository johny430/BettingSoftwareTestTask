import pytest
from tests.mocks import DUMMY_STATUS

@pytest.mark.asyncio
async def test_get_all_bets(bet_service, bet_repository_mock):
    result = await bet_service.get_all_bets()
    assert result == bet_repository_mock.get_all_bets.return_value
    bet_repository_mock.get_all_bets.assert_awaited_once()

@pytest.mark.asyncio
async def test_create_bet_event_not_found(bet_service, bet_repository_mock, event_repository_mock, dummy_bet):
    event_repository_mock.get_by_id.return_value = None
    result = await bet_service.create_bet(dummy_bet)
    assert result is None
    event_repository_mock.get_by_id.assert_awaited_once_with(dummy_bet.event_id)
    bet_repository_mock.create_bet.assert_not_awaited()

@pytest.mark.asyncio
async def test_update_status_by_event_id_success(bet_service, bet_repository_mock):
    event_id = 10
    new_status = DUMMY_STATUS

    result = await bet_service.update_status_by_event_id(event_id, new_status)
    assert result is True
    bet_repository_mock.update_bets_status_by_event_id.assert_awaited_once_with(event_id, new_status)
