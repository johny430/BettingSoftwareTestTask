from aio_pika import IncomingMessage

from repository.bet import BetRepository
from repository.event import EventRepository


async def process_created_events(event_repository: EventRepository, message: IncomingMessage):
    async with message.process():
        event = message.body.decode()
        await event_repository.add_event(event)


async def process_updated_events(bet_repository: BetRepository, message: IncomingMessage):
    async with message.process():
        body: dict = message.body.decode()
        await bet_repository.update_bet_status(body['id'], body['state'])
