from src.messaging.client import RabbitMQPublisher
from src.schemas.event import Event, EventStatusUpdate


class EventSenderRepository:
    def __init__(self, publisher: RabbitMQPublisher):
        self.publisher = publisher

    async def send_event_created_message(self, event: Event):
        await self.publisher.publish(event.model_dump_json(), "event.created")

    async def send_event_status_updated_message(self, event_status_update: EventStatusUpdate):
        await self.publisher.publish(event_status_update.model_dump_json(), "event.updated")
