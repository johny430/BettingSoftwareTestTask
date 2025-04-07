from pydantic import Field
from pydantic_settings import BaseSettings
from src.caching.settings import RedisSettings

from src.database.settings import PostgresqlSettings
from src.messaging.settings import RabbitMQSettings


class Settings(BaseSettings):
    host: str = Field(default="0.0.0.0")
    port: int = Field(default=8090)

    rabbitmq_settings: RabbitMQSettings = RabbitMQSettings()
    redis_settings: RedisSettings = RedisSettings()
    postgres_settings: PostgresqlSettings = PostgresqlSettings()

    class Config:
        env_file = ".env"
        extra = "allow"


settings = Settings()
