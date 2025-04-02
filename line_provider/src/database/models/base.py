import datetime

from sqlalchemy import MetaData, sql
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, registry

mapper_registry = registry(metadata=MetaData())


class BaseModel(DeclarativeBase):
    registry = mapper_registry
    metadata = mapper_registry.metadata


class TimedBaseModel(BaseModel):
    """
    An abstract base model that adds created_at and updated_at timestamp fields to the model
    """

    __abstract__ = True

    created_at: Mapped[datetime.datetime] = mapped_column(
        nullable=False, server_default=sql.func.now()
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        nullable=False,
        server_default=sql.func.now(),
        onupdate=sql.func.now(),
    )
