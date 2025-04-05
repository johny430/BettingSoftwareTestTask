from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    host: str = "127.0.0.1"
    port: int = 8090

    class Config:
        env_file = ".env"
        populate_by_name = True
        env_prefix = ""


app_settings = Settings()
