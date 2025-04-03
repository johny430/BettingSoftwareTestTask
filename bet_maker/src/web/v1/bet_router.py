from typing import Sequence

from fastapi import APIRouter, HTTPException, Depends

from schemas.bet import Bet, BetCreated, BetCreate
from schemas.event import Event
from services.bet import BetService
from services.dependecies import get_service

bet_router = APIRouter()


@bet_router.get("/events", response_model=Sequence[Event])
async def get_all_available_events():
    return []


@bet_router.post("/bet", response_model=BetCreated)
async def make_bet(
        bet_sum_dto: BetCreate,
        bet_service: BetService = Depends(get_service(BetService))
):
    new_bet_id = await bet_service.create_bet(bet_sum_dto)
    if new_bet_id is None:
        raise HTTPException(status_code=500, detail="Ошибка при создании ставки")
    return BetCreated(id=new_bet_id)


@bet_router.get("/bets", response_model=Sequence[Bet])
async def get_all_bets(bet_service: BetService = get_service(BetService)):
    return await bet_service.get_all_bets()
