from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings
from yarl import URL


class RabbitMQSettings(BaseSettings):
    host: str = Field(alias="RABBITMQ_HOST")
    port: int = Field(alias="RABBITMQ_PORT")
    user: str = Field(alias="RABBITMQ_USER")
    password: str = Field(alias="RABBITMQ_PASSWORD")
    vhost: str = Field(alias="RABBITMQ_VHOST")

    exchange_name: str = Field("guest", alias="RABBITMQ_EXCHANGE_NAME")
    routing_key: str = Field("guest", alias="RABBITMQ_ROUTING_KEY")

    @property
    def amqp_url(self) -> URL:
        return URL.build(
            scheme="amqp",
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            path=f"/{self.vhost}"
        )

    class Config:
        populate_by_name = True
        env_prefix = ""
        env_file = str(Path(__file__).resolve().parents[2] / ".env")
        extra = "allow"

rabbitmq_settings = RabbitMQSettings()
