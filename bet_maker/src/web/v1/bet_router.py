from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from bet_maker.src.database.dependencies import get_db_session
from bet_maker.src.database.models.bet import Bet
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
# @bet_router.post("/bet", response_model=BetIdDto)
# async def make_bet(
#     bet_sum_dto: BetCreateDto,
#     bet_gateway: Annotated[BetGateway, Depends(Stub(BetGateway))],
#     event_client: Annotated[EventClient, Depends(Stub(EventClient))],
# ):
#     new_bet_id = await bet_usecase.make_bet(
#         bet_gateway, event_client, bet_sum_dto.bet_sum, bet_sum_dto.event_id
#     )
#     return {"id": new_bet_id}
#

@bet_router.get("/bets", response_model=list[Bet])
async def get_all_bets(db: AsyncSession = Depends(get_db_session)):
    return await BetService.get_all_bets(db)