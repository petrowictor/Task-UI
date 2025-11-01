from typing import Self

from pydantic import HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_nested_delimiter='.'
    )

    app_url: HttpUrl
    headless: bool
    timeout: float

    @classmethod
    def initialize(cls) -> Self:
        return Settings()