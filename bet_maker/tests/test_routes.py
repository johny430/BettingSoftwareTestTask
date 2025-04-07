import pytest
from fastapi import HTTPException
from src.schemas.bet import BetCreated
from src.web.v1.bet_router import make_bet, get_all_bets


@pytest.mark.asyncio
async def test_make_bet_success_unit(sample_bet, mock_bet_service):
    mock_bet_service.create_bet.return_value = 123
    result = await make_bet(sample_bet, mock_bet_service)
    assert result == BetCreated(id=123)


@pytest.mark.asyncio
async def test_make_bet_failure_unit(sample_bet, mock_bet_service):
    mock_bet_service.create_bet.return_value = None
    with pytest.raises(HTTPException) as exc_info:
        await make_bet(sample_bet, mock_bet_service)
    assert exc_info.value.status_code == 500
    assert exc_info.value.detail == "Ошибка при создании ставки"


@pytest.mark.asyncio
async def test_get_all_bets_unit(sample_bets, mock_bet_service):
    mock_bet_service.get_all_bets.return_value = sample_bets
    result = await get_all_bets(mock_bet_service)
    assert result == sample_bets
