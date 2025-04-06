from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.caching.client import RedisClient
from src.caching.dependecies import get_redis_client
from src.database.dependencies import get_database_session
from src.services.bet import BetService
from src.services.event import EventService


def get_bet_service(
        database_session: AsyncSession = Depends(get_database_session),
        redis_client: RedisClient = Depends(get_redis_client)
):
    yield BetService(database_session, redis_client)


def get_event_service(redis_client: RedisClient = Depends(get_redis_client)):
    yield EventService(redis_client)
