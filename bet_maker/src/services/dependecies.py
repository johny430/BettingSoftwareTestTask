from fastapi import Depends
from sqlalchemy.orm import Session

from database.dependencies import get_db_session


def get_service(service_cls):
    def dependency(db: Session = Depends(get_db_session)):
        return service_cls(db)

    return dependency
