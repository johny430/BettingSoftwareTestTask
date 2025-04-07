from src.database.models.event import Event
from src.messaging.client import RabbitMQPublisher


class EventSenderRepository:
    def __init__(self, publisher: RabbitMQPublisher):
        self.publisher = publisher

    async def send_event_created_message(self, event: Event):
        await self.publisher.publish({
            "event_id": event.id,
            "coefficient": float(event.coefficient),
            "deadline": event.deadline.timestamp(),
            "state": event.status.value,
        }, "event.created")

    async def send_event_status_updated_message(self, event: Event):
        await self.publisher.publish({'event_id': event.id, 'state': event.status}, "event.updated")
