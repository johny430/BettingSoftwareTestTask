from typing import Sequence

from fastapi import APIRouter, HTTPException, Depends
from setuptools.dist import sequence

from schemas.bet import Bet, BetCreated, BetCreate
from schemas.event import Event
from services.bet import BetService
from services.dependecies import get_service

line_router = APIRouter()


@line_router.post("/", response_model=EventResponse, status_code=201)
def create_event(event_data: EventCreate, service: EventService = Depends(get_event_service)):
    return service.create_event(event_data)

@line_router.get("/{event_id}", response_model=EventResponse)
def get_event(event_id: int, service: EventService = Depends(get_event_service)):
    event = service.get_event_by_id(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@line_router.get("/", response_model=sequence[Event])
def get_events(service: EventService = Depends(get_service(Event))):
    return service.get_all_events()
