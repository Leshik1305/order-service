from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_PORT: int
    POSTGRES_CONNECTION_STRING: str
    BASE_URL: str
    API_KEY: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
