import os
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_PORT: int = 8000
    CALLBACK_URL: str = "https://leshik1305-order-service.dev-1.python-labs.ru/api"
    POSTGRES_CONNECTION_STRING: str
    BASE_URL: Optional[str] = "https://capashi.dev-1.python-labs.ru"
    API_KEY: Optional[str] = "px64kgKjUAwnRlHuGuE5mk0zF7gOkYHa6L12qTdjzTg"
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(__file__), "..", ".env"),
        env_file_encoding="utf-8",
    )
