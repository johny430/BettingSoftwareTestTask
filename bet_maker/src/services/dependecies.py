from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from caching.client import RedisClient
from caching.dependecies import get_redis_client
from database.dependencies import get_db_session
from database.factory import get_db
from services.bet import BetService
from services.event import EventService


def get_bet_service(database_session: AsyncSession = Depends(get_db_session)):
    yield BetService(database_session)


def get_event_service(redis_client: RedisClient = Depends(get_redis_client), asd = Depends(get_db)):
    print(asd)
    yield EventService(redis_client)
