from sqlalchemy.ext.asyncio import AsyncSession

from repository.base import BaseRepository


class BaseService:
    def __init__(self, repository_cls: type[BaseRepository], session: AsyncSession):
        self.repository = repository_cls(session)
