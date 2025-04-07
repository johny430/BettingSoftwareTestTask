import json

from aio_pika import IncomingMessage
from src.enums.converter import get_bet_status_based_on_event_status
from src.services.bet import BetService

from src.enums.event import EventStatus
from src.schemas.event import EventCreate
from src.services.event import EventService


async def process_created_events(message: IncomingMessage, event_service: EventService):
    async with message.process():
        await event_service.add_event(EventCreate(**json.loads(message.body.decode())))


async def process_updated_events(message: IncomingMessage, bet_service: BetService):
    async with message.process():
        body = json.loads(message.body.decode())
        if 'id' not in body or 'status' not in body:
            return
        await bet_service.update_status_by_event_id(
            body['id'],
            get_bet_status_based_on_event_status(EventStatus(body['status']))
        )
