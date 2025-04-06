from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings
from yarl import URL


class RedisSettings(BaseSettings):
    redis_host: str = Field(alias="REDIS_HOST")
    redis_port: int = Field(alias="REDIS_PORT")
    redis_password: str = Field(alias="REDIS_PASSWORD")
    redis_db: int = Field(alias="REDIS_DB")

    cache_ttl: int = 100
    event_cache_key: str = "cached_events"

    @property
    def redis_url(self) -> URL:
        return URL.build(
            scheme="redis",
            host=self.redis_host,
            port=self.redis_port,
            user=None,
            password=self.redis_password,
            path=f"/{self.redis_db}"
        )

    class Config:
        populate_by_name = True
        env_prefix = ""
        env_file = str(Path(__file__).resolve().parents[2] / ".env")
        extra = "allow"

redis_settings = RedisSettings()
