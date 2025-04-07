from datetime import datetime, timedelta

from src.enums.event import EventStatus


class DummyEvent:
    def __init__(self, id: int, coefficient: float, deadline: datetime, status: EventStatus):
        self.id = id
        self.coefficient = coefficient
        self.deadline = deadline
        self.status = status

    def __eq__(self, other):
        return (
                self.id == other.id and
                self.coefficient == other.coefficient and
                self.deadline == other.deadline and
                self.status == other.status
        )


DUMMY_EVENT = DummyEvent(
    id=1,
    coefficient=2.5,
    deadline=datetime.now() + timedelta(days=1),
    status=EventStatus.NEW  # Ensure that CREATED exists in your EventStatus enum.
)


class DummyEventCreate:
    def __init__(self, coefficient: float, deadline: datetime):
        self.coefficient = coefficient
        self.deadline = deadline


DUMMY_EVENT_CREATE = DummyEventCreate(
    coefficient=2.5,
    deadline=datetime.now() + timedelta(days=1)
)
