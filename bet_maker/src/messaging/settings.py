from pydantic import Field
from pydantic_settings import BaseSettings
from yarl import URL


class RabbitMQSettings(BaseSettings):
    host: str = Field("127.0.0.1", alias="RABBITMQ_HOST")
    port: int = Field(5672, alias="RABBITMQ_PORT")
    user: str = Field("guest", alias="RABBITMQ_USER")
    password: str = Field("guest", alias="RABBITMQ_PASSWORD")
    vhost: str = Field("mrm", alias="RABBITMQ_VHOST")

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


rabbitmq_settings = RabbitMQSettings()
