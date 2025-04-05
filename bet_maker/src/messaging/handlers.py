import json

from aio_pika import IncomingMessage

from services.bet import BetService


async def process_created_events(message: IncomingMessage):
    async with message.process():
        print(f"created: {message.body.decode()}")
        # event = message.body.decode()
        # await event_repository.add_event(event)


async def process_updated_events(message: IncomingMessage, bet_service: BetService):
    async with message.process():
        body = json.loads(message.body.decode())
        if 'event_id' not in body or 'state' not in body:
            return
        await bet_service.update_status_by_event_id(body['event_id'], body['state'])
        print("done")