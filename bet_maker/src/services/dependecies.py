from fastapi import Depends
from sqlalchemy.orm import Session

from database.dependencies import get_db_session


def get_service(service_cls, database_session: Session = Depends(get_db_session)):
    def dependency():
        return service_cls(database_session)
    return dependency
