from typing import Annotated, Sequence

from fastapi import APIRouter, Depends

from src.schemas.event import EventCreate, EventStatusUpdate, EventResponse
from src.services.dependecies import get_event_service
from src.services.event import EventService
from src.web.utils import get_or_raise

line_router = APIRouter()


@line_router.post("/", response_model=EventResponse, status_code=201)
async def create_event(event_data: EventCreate, event_service: Annotated[EventService, Depends(get_event_service)]):
    return await get_or_raise(
        await event_service.create_event(event_data),
        500,
        "Error during event creation"
    )


@line_router.get("/{event_id}", response_model=EventResponse)
async def get_event_by_id(event_id: int, event_service: Annotated[EventService, Depends(get_event_service)]):
    return await get_or_raise(
        await event_service.get_event_by_id(event_id),
        404,
        "Event not found"
    )


@line_router.post("/{id}/status", response_model=EventResponse)
async def update_event_status(
        event_status_update: Annotated[EventStatusUpdate, Depends(EventStatusUpdate.as_dependency)],
        event_service: Annotated[EventService, Depends(get_event_service)]
):
    return await get_or_raise(
        await event_service.update_event_status(event_status_update),
        404,
        "Error during event status update"
    )


@line_router.get("/", response_model=Sequence[EventResponse])
async def get_events(event_service: Annotated[EventService, Depends(get_event_service)]):
    return await event_service.get_all_events()
