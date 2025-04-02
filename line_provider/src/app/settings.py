from pydantic import Field
from pydantic_settings import BaseSettings
from yarl import URL


class Settings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 8000

    db_host: str = Field("127.0.0.1", alias="POSTGRES_HOST")
    db_port: int = Field(5432, alias="POSTGRES_PORT")
    db_user: str = Field("postgres", alias="POSTGRES_USER")
    db_pass: str = Field("1234", alias="POSTGRES_PASSWORD")
    db_base: str = Field("mrm_db", alias="POSTGRES_DB")

    rabbitmq_host: str = Field("localhost", alias="POSTGRES_HOST")
    rabbitmq_port: int = Field(5532, alias="POSTGRES_PORT")
    rabbitmq_user: str = Field("postgres", alias="POSTGRES_USER")
    rabbitmq_pass: str = Field("postgres", alias="POSTGRES_PASSWORD")
    rabbitmq_base: str = Field("postgres", alias="POSTGRES_DB")

    redis_host: str = Field("localhost", alias="POSTGRES_HOST")
    redis_port: int = Field(5532, alias="POSTGRES_PORT")
    redis_user: str = Field("postgres", alias="POSTGRES_USER")
    redis_pass: str = Field("postgres", alias="POSTGRES_PASSWORD")
    redis_base: str = Field("postgres", alias="POSTGRES_DB")

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

    @property
    def ampq_url(self) -> URL:
        return URL.build(
            scheme="postgresql+asyncpg",
            host=self.db_host,
            port=self.db_port,
            user=self.db_user,
            password=self.db_pass,
            path=f"/{self.db_base}"
        )

    @property
    def redis_url(self) -> URL:
        return URL.build(
            scheme="postgresql+asyncpg",
            host=self.db_host,
            port=self.db_port,
            user=self.db_user,
            password=self.db_pass,
            path=f"/{self.db_base}"
        )

    class Config:
        env_file = ".env"


settings = Settings()
