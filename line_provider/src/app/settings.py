from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 8080

    class Config:
        env_file = ".env"
        extra = "allow"


app_settings = Settings()
