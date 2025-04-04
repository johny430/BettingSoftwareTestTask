import aio_pika
from aio_pika import ExchangeType

from src.messaging.settings import rabbitmq_settings


class RabbitMQClient:
    def __init__(self):
        self.queue_created = None
        self.queue_status_updated = None
        self.connection = None
        self.channel = None
        self.exchange = None
        self.on_message = None

    async def connect(self) -> None:
        self.connection = await aio_pika.connect_robust(rabbitmq_settings.amqp_url)
        self.channel = await self.connection.channel()
        self.exchange = await self.channel.declare_exchange(
            rabbitmq_settings.exchange_name, ExchangeType.TOPIC
        )

    async def declare_queues(self):
        async with self.connection:
            self.queue_created = await self.channel.declare_queue("event_created_queue", durable=True)
            await self.queue_created.bind(self.exchange, routing_key="event.created")
            self.queue_status_updated = await self.channel.declare_queue("event_status_updated_queue", durable=True)
            await self.queue_status_updated.bind(self.exchange, routing_key="event.status.updated")

    async def consume(self, queue_created_handler, queue_status_updated_handler):
        await self.queue_created.consume(queue_created_handler)
        await self.queue_status_updated.consume(queue_status_updated_handler)

    async def close(self) -> None:
        if self.connection:
            await self.connection.close()
