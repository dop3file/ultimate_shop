from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr, Field
from dotenv import load_dotenv

import os


class Config(BaseSettings):
    auth_secret_key: str = Field()
    algorithm: str = Field()
    expiration_time: int = Field()
    database_url: str = Field()


load_dotenv()
config = Config(
    auth_secret_key=os.getenv("AUTH_SECRET_KEY"),
    algorithm="HS256",
    expiration_time=1800,
    database_url=os.getenv("DATABASE_URL")
)
