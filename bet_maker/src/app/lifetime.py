from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    async with app.state.db_engine.begin() as conn:
        await conn.run_sync(meta.create_all)

    yield

    await app.state.db_engine.dispose()