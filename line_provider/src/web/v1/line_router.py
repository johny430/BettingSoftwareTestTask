from typing import Sequence

from fastapi import APIRouter, HTTPException, Depends

from services.dependecies import get_service
from src.schemas.event import EventResponse, EventCreate, EventUpdateStatus
from src.services.event import EventService

line_router = APIRouter()


@line_router.post("/", response_model=EventResponse, status_code=201)
def create_event(event_data: EventCreate, event_service: EventService = Depends(get_service(EventService))):
    return event_service.create_event(event_data)


@line_router.get("/{event_id}", response_model=EventResponse)
def get_event(event_id: int, event_service: EventService = Depends(get_service(EventService))):
    event = event_service.get_event_by_id(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@line_router.get("/", response_model=Sequence[EventResponse])
def get_events(event_service: EventService = Depends(get_service(EventService))):
    return event_service.get_all_events()


@line_router.patch("/{event_id}/status", response_model=EventResponse)
async def update_event_status(
        event_id: int,
        status_update: EventUpdateStatus,
        event_service: EventService = Depends(get_service(EventService))
):
    event = await event_service.update_event_status(event_id, status_update.state)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event
