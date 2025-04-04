from pydantic import Field
from pydantic_settings import BaseSettings
from sqlalchemy import URL


class RedisSettings(BaseSettings):
    redis_host: str = Field("localhost", alias="REDIS_HOST")
    redis_port: int = Field(6379, alias="REDIS_PORT")
    redis_password: str = Field("", alias="REDIS_PASSWORD")
    redis_db: int = Field(0, alias="REDIS_DB")

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


redis_settings = RedisSettings()
