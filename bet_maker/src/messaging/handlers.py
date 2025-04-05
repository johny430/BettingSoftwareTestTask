from aio_pika import IncomingMessage


async def process_created_events(message: IncomingMessage):
    async with message.process():
        print(f"created: {message.body.decode()}")
        # event = message.body.decode()
        # await event_repository.add_event(event)


async def process_updated_events(message: IncomingMessage):
    async with message.process():
        print(f"updated: {message.body.decode()}")
        # body: dict = message.body.decode()
        # await bet_repository.update_bet_status(body['id'], body['state'])
