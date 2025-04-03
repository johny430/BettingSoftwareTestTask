from typing import Type, TypeVar, Callable

from fastapi import Depends
from sqlalchemy.orm import Session

from database.dependencies import get_db_session

Service = TypeVar("Service")  # Service type


def get_service(service_cls: Type[Service], db: Session = Depends(get_db_session)) -> Callable[[Session], Service]:
    return service_cls(db)
