from fastapi import FastAPI

from bet_maker.src.app.lifetime import lifespan
from bet_maker.src.web.router import router


def get_app() -> FastAPI:
    app = FastAPI(
        lifespan=lifespan,
        version="1.0.0",
        docs_url="/api/docs",
    )
    app.include_router(router=router, prefix="/api")

    return app
