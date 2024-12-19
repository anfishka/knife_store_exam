from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./knives.db"
    JWT_SECRET: str = "SECRET"
    JWT_ALGORITHM: str = "HS256"
    TELEGRAM_BOT_TOKEN: str
    TELEGRAM_CHAT_ID: str

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent / ".env",
        env_file_encoding="utf-8",
    )

settings = Settings()
