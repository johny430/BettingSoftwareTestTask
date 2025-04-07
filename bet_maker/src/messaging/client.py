import aio_pika
from aio_pika import ExchangeType

from src.app.settings import settings


class RabbitMQClient:
    def __init__(self):
        self.amqp_url = settings.rabbitmq_settings.amqp_url
        self.exchange_name = settings.rabbitmq_settings.exchange_name
        self.event_created_queue = None
        self.event_status_updated_queue = None
        self.connection = None
        self.channel = None
        self.exchange = None

    async def connect(self) -> None:
        self.connection = await aio_pika.connect_robust(self.amqp_url)
        self.channel = await self.connection.channel()
        self.exchange = await self.channel.declare_exchange(self.exchange_name, ExchangeType.TOPIC)

    async def declare_queues(self) -> None:
        self.event_created_queue = await self.channel.declare_queue("event_created_queue", durable=True)
        await self.event_created_queue.bind(self.exchange, routing_key="event.created")
        self.event_status_updated_queue = await self.channel.declare_queue("event_status_updated_queue", durable=True)
        await self.event_status_updated_queue.bind(self.exchange, routing_key="event.updated")

    async def consume(self, queue1_handler, queue2_handler) -> None:
        await self.event_created_queue.consume(queue1_handler)
        await self.event_status_updated_queue.consume(queue2_handler)

    async def close(self) -> None:
        await self.connection.close()
