import json

import aio_pika
from aio_pika import ExchangeType, Message

from src.messaging.settings import rabbitmq_settings


class RabbitMQPublisher:
    def __init__(self):
        self.connection = None
        self.channel = None
        self.exchange = None

    async def connect(self) -> None:
        self.connection = await aio_pika.connect_robust(rabbitmq_settings.amqp_url)
        self.channel = await self.connection.channel()
        self.exchange = await self.channel.declare_exchange(
            rabbitmq_settings.exchange_name, ExchangeType.TOPIC
        )

    async def publish(self, message_body: dict) -> None:
        if not self.exchange:
            await self.connect()
        await self.exchange.publish(Message(json.dumps(message_body).encode()),
                                    routing_key=rabbitmq_settings.routing_key)

    async def close(self) -> None:
        if self.connection:
            await self.connection.close()
