from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from yarl import URL


class PostgresqlSettings(BaseSettings):
    host: str = Field(alias="POSTGRES_HOST")
    port: int = Field(alias="POSTGRES_PORT")
    user: str = Field(alias="POSTGRES_USER")
    password: str = Field(alias="POSTGRES_PASSWORD")
    database: str = Field(alias="POSTGRES_DB")

    @property
    def db_url(self) -> URL:
        return URL.build(
            scheme="postgresql+asyncpg",
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            path=f"/{self.database}"
        )

    model_config = SettingsConfigDict(env_file=".env", extra="allow")
