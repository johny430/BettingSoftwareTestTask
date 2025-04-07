from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from repository.event import EventRepository
from src.database.dependencies import get_database_session
from src.messaging.client import RabbitMQPublisher
from src.messaging.dependecies import get_rabbitmq_client
from src.repository.event_sender import EventSenderRepository
from src.services.event import EventService


def get_event_service(
        database_session: AsyncSession = Depends(get_database_session),
        publisher: RabbitMQPublisher = Depends(get_rabbitmq_client)
):
    yield EventService(EventRepository(database_session), EventSenderRepository(publisher))
