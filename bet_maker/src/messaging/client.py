import asyncio

import aio_pika


async def on_message(message):
    async with message.process():
        print("Received message:", message.body.decode())


async def main():
    # Connect to RabbitMQ (adjust connection URL as needed)
    connection = await aio_pika.connect_robust("amqp://guest:guest@localhost/")
    async with connection:
        channel = await connection.channel()
        # Declare a topic exchange
        exchange = await channel.declare_exchange("events_exchange", aio_pika.ExchangeType.TOPIC)

        # Declare and bind the queue for event creations
        queue_created = await channel.declare_queue("event_created_queue", durable=True)
        await queue_created.bind(exchange, routing_key="event.created")

        # Declare and bind the queue for status updates
        queue_status_updated = await channel.declare_queue("event_status_updated_queue", durable=True)
        await queue_status_updated.bind(exchange, routing_key="event.status.updated")

        # Start consuming messages from both queues
        await queue_created.consume(on_message)
        await queue_status_updated.consume(on_message)

        print(" [*] Waiting for messages. To exit press CTRL+C")
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
