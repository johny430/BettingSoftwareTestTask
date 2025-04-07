from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings
from yarl import URL


class PostgresqlSettings(BaseSettings):
    db_host: str = Field(alias="POSTGRES_HOST")
    db_port: int = Field(alias="POSTGRES_PORT")
    db_user: str = Field(alias="POSTGRES_USER")
    db_pass: str = Field(alias="POSTGRES_PASSWORD")
    db_base: str = Field(alias="POSTGRES_DB")

    @property
    def db_url(self) -> URL:
        return URL.build(
            scheme="postgresql+asyncpg",
            host=self.db_host,
            port=self.db_port,
            user=self.db_user,
            password=self.db_pass,
            path=f"/{self.db_base}"
        )

    class Config:
        # env_file = str(Path(__file__).resolve().parents[2] / ".env")
        env_file = ".env"
        extra = "allow"
