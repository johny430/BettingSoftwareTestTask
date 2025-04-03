from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


async def get_repository(db: AsyncSession = Depends(get_db)) -> MyRepository:
    return MyRepository(db)