from messaging.client import RabbitMQClient
from messaging.handlers import process_updated_events, process_created_events

if __name__ == '__main__':
    import asyncio


    async def main():

        client = RabbitMQClient()
        await client.connect()
        await client.declare_queues()
        await client.consume(process_created_events, process_updated_events)

        print("Waiting for messages")
        try:
            await asyncio.Future()
        except asyncio.CancelledError:
            pass
        finally:
            await client.close()


    asyncio.run(main())
