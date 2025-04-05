from functools import partial

from caching.client import RedisClient
from database.dependencies import create_database_connection
from messaging.client import RabbitMQClient
from messaging.handlers import process_updated_events, process_created_events
from services.bet import BetService
from services.event import EventService


async def main():
    rabbitmq_client = RabbitMQClient()

    redis_client = RedisClient()
    await redis_client.connect()
    engine, session_factory = create_database_connection()

    event_service = EventService(redis_client)
    bet_service = BetService(session_factory(), redis_client)

    await rabbitmq_client.connect()
    await rabbitmq_client.declare_queues()
    await rabbitmq_client.consume(process_created_events, partial(process_updated_events, bet_service=bet_service))

    print("Waiting for messages")
    try:
        await asyncio.Future()
    except asyncio.CancelledError:
        pass
    finally:
        await rabbitmq_client.close()
        await redis_client.close()
        await engine.dispose()


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
