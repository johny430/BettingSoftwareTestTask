from typing import Sequence, Annotated

from fastapi import APIRouter, HTTPException, Depends

from schemas.bet import BetResponse, BetCreated, BetCreate
from services.bet import BetService
from services.dependecies import get_event_service, get_bet_service
from services.event import EventService

bet_router = APIRouter()


@bet_router.get("/events")
async def get_all_available_events(event_service: Annotated[EventService, Depends(get_event_service)]):
    return await event_service.get_all()


@bet_router.post("/bet", response_model=BetCreated)
async def make_bet(
        bet_sum_dto: BetCreate,
        bet_service: Annotated[BetService, Depends(get_bet_service)]
):
    new_bet_id = await bet_service.create_bet(bet_sum_dto)
    if new_bet_id is None:
        raise HTTPException(status_code=500, detail="Ошибка при создании ставки")
    return BetCreated(id=new_bet_id)


@bet_router.get("/bets", response_model=Sequence[BetResponse])
async def get_all_bets(bet_service: Annotated[BetService, Depends(get_bet_service)]):
    return await bet_service.get_all_bets()
