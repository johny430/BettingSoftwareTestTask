from typing import Sequence, Annotated

from fastapi import APIRouter, HTTPException, Depends
from src.schemas.bet import BetResponse, BetCreate
from src.services.bet import BetService

from schemas.event import Event
from src.services.dependecies import get_event_service, get_bet_service
from src.services.event import EventService

bet_router = APIRouter()


@bet_router.get("/events", response_model=Sequence[Event])
async def get_all_available_events(event_service: Annotated[EventService, Depends(get_event_service)]):
    return await event_service.get_all()


@bet_router.post("/bet", response_model=BetResponse)
async def make_bet(
        bet: BetCreate,
        bet_service: Annotated[BetService, Depends(get_bet_service)]
):
    created_bet = await bet_service.create_bet(bet)
    if created_bet is None:
        raise HTTPException(status_code=500, detail="Ошибка при создании ставки")
    return created_bet


@bet_router.get("/bets", response_model=Sequence[BetResponse])
async def get_all_bets(bet_service: Annotated[BetService, Depends(get_bet_service)]):
    return await bet_service.get_all_bets()


@bet_router.get("/bet/{bet_id}", response_model=BetResponse)
async def get_all_bets(bet_id: int, bet_service: Annotated[BetService, Depends(get_bet_service)]):
    bet = await bet_service.get_by_id(bet_id)
    if bet is None:
        raise HTTPException(status_code=404, detail="Bet not found")
    return bet
