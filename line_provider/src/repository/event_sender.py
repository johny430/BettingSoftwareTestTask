from src.database.models.event import Event
from src.messaging.client import RabbitMQPublisher


class EventsenderRepository:
    def __init__(self, publisher: RabbitMQPublisher):
        self.publisher = publisher

    async def send_event_status_updated_message(self, event: Event):
        await self.publisher.publish({
            "event_id": event.id,
            "coefficient": float(event.coefficient),
            "deadline": event.deadline.timestamp(),
            "state": event.state.value,
        }, "event.updated")

    async def send_event_created_message(self, event: Event):
        await self.publisher.publish({'event_id': event.id, 'state': event.state}, "event.created")
