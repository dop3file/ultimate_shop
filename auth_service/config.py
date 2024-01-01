from datetime import timedelta

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr, Field
from dotenv import load_dotenv

import os


class Config(BaseSettings):
    auth_secret_key: str = Field()
    hash_algorithm: str = Field()
    expiration_time: int = Field()
    database_url: str = Field()
    token_expire: timedelta
    sentry_url: str = Field()


load_dotenv()
config = Config(
    auth_secret_key=os.getenv("AUTH_SECRET_KEY"),
    hash_algorithm="HS256",
    expiration_time=1800,
    database_url=os.getenv("DATABASE_URL"),
    token_expire=timedelta(minutes=30),
    sentry_url=os.getenv("SENTRY_URL")
)
