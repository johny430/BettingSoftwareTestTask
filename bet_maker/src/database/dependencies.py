from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request


async def get_db_session(request: Request) -> AsyncGenerator[AsyncSession, None]:
    async with request.app.state.db_session_factory() as session:
        try:
            yield session
        except Exception as e:
            await session.rollback()
        finally:
            await session.commit()
            await session.close()
