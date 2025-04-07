from fastapi import FastAPI

from src.app.lifetime import lifespan
from src.web.router import router


def get_app() -> FastAPI:
    app = FastAPI(
        lifespan=lifespan,
        version="1.0.0",
        docs_url="/api/docs",
        title="Line Provider"
    )
    app.include_router(router=router, prefix="/api")

    return app
