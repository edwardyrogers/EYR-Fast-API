import os

from dotenv import load_dotenv

from app.config.env_config import Settings


class EnvService:
    def __init__(self):
        self.env: str = "dev"
        self.settings: Settings = Settings()

    def load(self) -> str:
        self.env = os.getenv("FASTAPI_ENV", "dev")
        load_dotenv(f".env.{self.env}")
        self.settings = Settings()
        return self.settings
