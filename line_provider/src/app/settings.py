from pydantic import Field
from pydantic_settings import BaseSettings

from src.database.settings import PostgresqlSettings
from src.messaging.settings import RabbitMQSettings


class Settings(BaseSettings):
    host: str = Field(default="0.0.0.0")
    port: int = Field(default=8080)

    rabbitmq_settings: RabbitMQSettings = RabbitMQSettings()
    postgres_settings: PostgresqlSettings = PostgresqlSettings()

    class Config:
        env_file = ".env"
        extra = "allow"


settings = Settings()
