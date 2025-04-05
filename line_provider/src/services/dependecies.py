from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.dependencies import get_database_session
from src.messaging.client import RabbitMQPublisher
from src.messaging.dependecies import get_rabbitmq_client
from src.services.event import EventService


def get_event_service(
        database_session: AsyncSession = Depends(get_database_session),
        publisher: RabbitMQPublisher = Depends(get_rabbitmq_client)
):
    yield EventService(database_session, publisher)
