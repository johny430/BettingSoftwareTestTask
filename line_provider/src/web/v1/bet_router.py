from typing import Sequence

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database.dependencies import get_db_session
from schemas.bet import Bet, BetCreated, BetCreate
from schemas.event import Event
from services.bet import BetService

bet_router = APIRouter()


@bet_router.get("/events", response_model=Sequence[Event])
async def get_all_available_events():
    return []


@bet_router.post("/bet", response_model=BetCreated)
async def make_bet(
        bet_sum_dto: BetCreate,
        db: AsyncSession = Depends(get_db_session)
):
    new_bet_id = await BetService.create_bet(db, bet_sum_dto)
    if new_bet_id is None:
        raise HTTPException(status_code=500, detail="Ошибка при создании ставки")
    return BetCreated(id=new_bet_id)


@bet_router.get("/bets", response_model=Sequence[Bet])
async def get_all_bets(db: AsyncSession = Depends(get_db_session)):
    return await BetService.get_all_bets(db)
