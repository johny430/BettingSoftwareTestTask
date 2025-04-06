from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 8090

    class Config:
        env_file = str(Path(__file__).resolve().parents[2] / ".env")
        populate_by_name = True
        env_prefix = ""
        extra = "allow"

app_settings = Settings()
