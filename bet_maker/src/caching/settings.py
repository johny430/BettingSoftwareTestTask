from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from yarl import URL


class RedisSettings(BaseSettings):
    host: str = Field(alias="REDIS_HOST")
    port: int = Field(alias="REDIS_PORT")
    db: int = Field(alias="REDIS_DB")

    event_cache_key: str = Field(default="cached_events")

    @property
    def redis_url(self) -> URL:
        return URL.build(
            scheme="redis",
            host=self.host,
            port=self.port,
            path=f"/{self.db}"
        )

    model_config = SettingsConfigDict(env_file=".env", extra="allow")
