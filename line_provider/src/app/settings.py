from pydantic import Field
from pydantic_settings import BaseSettings
from yarl import URL


class PostgresqlSettings(BaseSettings):
    db_host: str = Field("127.0.0.1", alias="POSTGRES_HOST")
    db_port: int = Field(5432, alias="POSTGRES_PORT")
    db_user: str = Field("postgres", alias="POSTGRES_USER")
    db_pass: str = Field("1234", alias="POSTGRES_PASSWORD")
    db_base: str = Field("mrm_db", alias="POSTGRES_DB")

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
        # Allow environment variables to be set via their alias names.
        populate_by_name = True
        env_prefix = ""


class RabbitmqSettings(BaseSettings):
    rabbitmq_host: str = Field("localhost", alias="RABBITMQ_HOST")
    rabbitmq_port: int = Field(5672, alias="RABBITMQ_PORT")
    rabbitmq_user: str = Field("guest", alias="RABBITMQ_USER")
    rabbitmq_pass: str = Field("guest", alias="RABBITMQ_PASSWORD")
    rabbitmq_vhost: str = Field("/", alias="RABBITMQ_VHOST")

    @property
    def amqp_url(self) -> URL:
        return URL.build(
            scheme="amqp",
            host=self.rabbitmq_host,
            port=self.rabbitmq_port,
            user=self.rabbitmq_user,
            password=self.rabbitmq_pass,
            path=self.rabbitmq_vhost
        )

    class Config:
        populate_by_name = True
        env_prefix = ""


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


class Settings(BaseSettings):
    host: str = "127.0.0.1"
    port: int = 8080

    postgresql_settings: PostgresqlSettings = PostgresqlSettings()
    rabbitmq_settings: RabbitmqSettings = RabbitmqSettings()
    redis_settings: RedisSettings = RedisSettings()

    class Config:
        env_file = ".env"
        populate_by_name = True
        env_prefix = ""


settings = Settings()
