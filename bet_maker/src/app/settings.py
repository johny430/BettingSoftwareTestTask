from pathlib import Path

from pydantic_settings import BaseSettings
from src.caching.settings import RedisSettings

from src.database.settings import PostgresqlSettings
from src.messaging.settings import RabbitMQSettings


class Settings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 8090

    rabbitmq_settings: RabbitMQSettings = RabbitMQSettings()
    redis_settings: RedisSettings = RedisSettings()
    postgres_settings: PostgresqlSettings = PostgresqlSettings()

    class Config:
        env_file = str(Path(__file__).resolve().parents[2] / ".env")
        extra = "allow"


settings = Settings()
