"""App settings, read from environment variables / the .env file.

pydantic-settings matches each field to an env var with the same name
(case-insensitive) and validates its type. This keeps secrets out of the code.
"""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="../.env", extra="ignore")

    app_name: str = "Study OS AI"
    database_url: str = "postgresql+psycopg://studyos:studyos@localhost:5432/studyos"
    redis_url: str = "redis://localhost:6379/0"


settings = Settings()  # one shared instance, imported everywhere
