from fastapi import FastAPI

from src.messaging.client import RabbitMQPublisher


async def setup_rabbitmq(app: FastAPI) -> None:
    app.state.publisher = RabbitMQPublisher()
    await app.state.publisher.connect()
