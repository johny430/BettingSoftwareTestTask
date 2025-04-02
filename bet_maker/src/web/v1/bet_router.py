from typing import Sequence

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from bet_maker.src.database.dependencies import get_db_session
from bet_maker.src.schemas.bet import Bet, BetCreated, BetCreate
from bet_maker.src.services.bet import BetService

bet_router = APIRouter()


# @bet_router.get("/events", response_model=list[Event])
# async def get_all_available_events(
#     event_client: Annotated[EventClient, Depends(Stub(EventClient))]
# ):
#     all_available_events = await bet_usecase.get_all_available_events(event_client)
#     return all_available_events
#
#
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
