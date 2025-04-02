import uvicorn

from bet_maker.src.app.settings import settings


def main() -> None:
    uvicorn.run(
        "bet_maker.src.app.application:get_app",
        host=settings.host,
        port=settings.port,
        factory=True,
    )


if __name__ == "__main__":
    main()
