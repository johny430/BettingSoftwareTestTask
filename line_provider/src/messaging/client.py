import aio_pika
from aio_pika import ExchangeType, Message

from src.app.settings import settings


class RabbitMQPublisher:
    def __init__(self):
        self.connection = None
        self.channel = None
        self.exchange = None

    async def connect(self) -> None:
        self.connection = await aio_pika.connect_robust(settings.rabbitmq_settings.amqp_url)
        self.channel = await self.connection.channel()
        self.exchange = await self.channel.declare_exchange(
            settings.rabbitmq_settings.exchange_name, ExchangeType.TOPIC
        )

    async def publish(self, message_body: str, routing_key: str) -> None:
        await self.exchange.publish(Message(message_body.encode()), routing_key=routing_key)

    async def close(self) -> None:
        await self.connection.close()
