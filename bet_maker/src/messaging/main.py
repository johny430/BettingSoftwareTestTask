import asyncio

from caching.client import RedisClient
from messaging.client import RabbitMQClient
from messaging.handlers import process_created_events, process_updated_events


async def main():
    rabbitmq_client = RabbitMQClient()
    redis_client = RedisClient()
    await redis_client.connect()

    await rabbitmq_client.connect()
    await rabbitmq_client.declare_queues()
    await rabbitmq_client.consume(process_created_events, process_updated_events)
    print(" [*] Waiting for messages. To exit press CTRL+C")
    await asyncio.Future()  # Run forever


if __name__ == '__main__':
    asyncio.run(main())
