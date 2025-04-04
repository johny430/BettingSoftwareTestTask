from src.messaging.client import RabbitMQPublisher


class EventsenderRepository:
    def __int__(self, publisher: RabbitMQPublisher):
        self.publisher = publisher

    async def send_event_status_updated_message(self, event):
        await self.publisher.publish(event, "event.updated")

    async def send_event_created_message(self, event):
        await self.publisher.publish(event, "event.created")