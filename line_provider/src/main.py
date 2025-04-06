import uvicorn

from src.app.settings import app_settings


def main() -> None:
    uvicorn.run(
        "src.app.application:get_app",
        host=app_settings.host,
        port=app_settings.port,
        factory=True,
    )


if __name__ == "__main__":
    main()
