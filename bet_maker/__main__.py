import uvicorn

from bet_maker.src.app.settings import settings


def main() -> None:
    if settings.reload:
        uvicorn.run(
            "bet_maker.app.application:get_app",
            workers=settings.workers_count,
            host=settings.host,
            port=settings.port,
            reload=settings.reload,
            log_level=settings.log_level.value.lower(),
            factory=True,
        )


if __name__ == "__main__":
    main()
