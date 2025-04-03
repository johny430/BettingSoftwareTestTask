from fastapi import APIRouter, HTTPException, Depends

from src.enums.event import EventState
from src.schemas.event import EventCreate
from src.services.dependecies import get_service
from src.services.event import EventService

line_router = APIRouter()


@line_router.post("/", status_code=201)
async def create_event(event_data: EventCreate, event_service: EventService = Depends(get_service(EventService))):
    created_event = await event_service.create_event(event_data)
    if created_event is None:
        raise HTTPException(status_code=500, detail="Error during event creation")
    return created_event


@line_router.get("/{event_id}")
async def get_event(event_id: int, event_service: EventService = Depends(get_service(EventService))):
    event = await event_service.get_event_by_id(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@line_router.get("/")
async def get_events(event_service: EventService = Depends(get_service(EventService))):
    return await event_service.get_all_events()


@line_router.post("/{event_id}/status")
async def update_event_status(
        event_id: int,
        status: EventState,
        event_service: EventService = Depends(get_service(EventService))
):
    updated_event = await event_service.update_event_status(event_id, status)
    if not updated_event:
        raise HTTPException(status_code=404, detail="Error during event status update")
    return updated_event
