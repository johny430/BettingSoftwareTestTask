from fastapi import FastAPI

from app.lifetime import lifespan
from web.router import router


def get_app() -> FastAPI:
    app = FastAPI(
        lifespan=lifespan,
        version="1.0.0",
        docs_url="/api/docs",
        title="Bet Maker"
    )
    app.include_router(router=router, prefix="/api")

    return app
