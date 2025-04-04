from fastapi import APIRouter, Depends

from src.enums.event import EventState
from src.schemas.event import EventCreate
from src.services.dependecies import get_service
from src.services.event import EventService
from src.web.utils import get_or_raise

line_router = APIRouter()


@line_router.post("/", status_code=201)
async def create_event(event_data: EventCreate, event_service: EventService = Depends(get_service(EventService))):
    return await get_or_raise(
        await event_service.create_event(event_data),
        500,
        "Error during event creation"
    )


@line_router.get("/{event_id}")
async def get_event(event_id: int, event_service: EventService = Depends(get_service(EventService))):
    return await get_or_raise(
        await event_service.get_event_by_id(event_id),
        404,
        "Event not found"
    )


@line_router.post("/{event_id}/status")
async def update_event_status(
        event_id: int,
        status: EventState,
        event_service: EventService = Depends(get_service(EventService))
):
    return await get_or_raise(
        await event_service.update_event_status(event_id, status),
        404,
        "Error during event status update"
    )


@line_router.get("/")
async def get_events(event_service: EventService = Depends(get_service(EventService))):
    return await event_service.get_all_events()
