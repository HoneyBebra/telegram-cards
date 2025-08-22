from functools import lru_cache
from logging import config as logging_config
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

from .logger import LOGGING

load_dotenv()

BASE_DIR = Path(__file__).parent.parent.parent
ENV_FILE = BASE_DIR / ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=ENV_FILE)

    bot_token: str

    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_port: int


class Commands(BaseSettings):
    add_card_command: str = "Добавить карточку"
    learn_cards_command: str = "Учить карточки"


@lru_cache
def get_settings() -> Settings:
    return Settings()  # type: ignore[call-arg]


def get_commands() -> Commands:
    return Commands()


settings = get_settings()
commands = get_commands()


logging_config.dictConfig(LOGGING)
