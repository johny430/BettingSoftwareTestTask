import json

from aio_pika import IncomingMessage

from enums.converter import get_bet_status_base_on_event_state
from enums.event import EventState
from schemas.event import EventSchema
from services.bet import BetService
from services.event import EventService


async def process_created_events(message: IncomingMessage, event_service: EventService):
    async with message.process():
        body = json.loads(message.body.decode())
        await event_service.add_event(EventSchema(
            id=body['event_id'],
            coefficient=body['coefficient'],
            deadline=int(body['deadline']),
            state=body['state']
        ))


async def process_updated_events(message: IncomingMessage, bet_service: BetService):
    async with message.process():
        body = json.loads(message.body.decode())
        if 'event_id' not in body or 'state' not in body:
            return
        await bet_service.update_status_by_event_id(
            body['event_id'],
            get_bet_status_base_on_event_state(EventState(body['state']))
        )
