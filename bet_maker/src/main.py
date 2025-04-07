import uvicorn

from src.app.settings import settings


def main() -> None:
    uvicorn.run(
        "app.application:get_app",
        host=settings.host,
        port=settings.port,
        factory=True,
    )


if __name__ == "__main__":
    main()
