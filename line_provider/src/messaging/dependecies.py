from fastapi import FastAPI
from starlette.requests import Request

from src.messaging.client import RabbitMQPublisher


async def setup_rabbitmq(app: FastAPI) -> None:
    app.state.publisher = RabbitMQPublisher()
    await app.state.publisher.connect()


async def get_rabbitmq_client(request: Request):
    yield request.app.state.publisher
