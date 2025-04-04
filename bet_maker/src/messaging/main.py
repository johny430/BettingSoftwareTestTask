import asyncio
from functools import partial

from caching.client import RedisClient
from database.dependencies import get_db_session
from database.factory import start_database_connection
from messaging.client import RabbitMQClient
from messaging.handlers import process_created_events, process_updated_events
from repository.bet import BetRepository
from repository.event import EventRepository


async def main():
    rabbitmq_client = RabbitMQClient()

    redis_client = RedisClient()
    await redis_client.connect()

    engine, session_factory = start_database_connection()

    await rabbitmq_client.connect()
    await rabbitmq_client.declare_queues()
    await rabbitmq_client.consume(
        partial(process_created_events, EventRepository(redis_client)),
        partial(process_updated_events, BetRepository(next(get_db_session(session_factory))))
    )
    print(" [*] Waiting for messages. To exit press CTRL+C")
    await asyncio.Future()  # Run forever


if __name__ == '__main__':
    asyncio.run(main())
