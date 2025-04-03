from pydantic import Field
from pydantic_settings import BaseSettings
from yarl import URL


class RabbitMQSettings(BaseSettings):
    host: str = Field("rabbitmq", alias="RABBITMQ_HOST")
    port: int = Field(5672, alias="RABBITMQ_PORT")
    user: str = Field("guest", alias="RABBITMQ_USER")
    password: str = Field("guest", alias="RABBITMQ_PASSWORD")

    exchange_name: str = Field("guest", alias="RABBITMQ_EXCHANGE_NAME")
    routing_key: str = Field("guest", alias="RABBITMQ_ROUTING_KEY")

    @property
    def amqp_url(self) -> URL:
        return URL.build(
            scheme="amqp",
            host=self.rabbitmq_host,
            port=self.rabbitmq_port,
            user=self.rabbitmq_user,
            password=self.rabbitmq_pass
        )

    class Config:
        populate_by_name = True
        env_prefix = ""


rabbitmq_settings = RabbitMQSettings()
