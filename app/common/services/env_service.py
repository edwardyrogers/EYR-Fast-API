import os

from dotenv import load_dotenv
from app.common.services.logging_service import LoggingService
from app.config.env_config import Settings


class EnvService:
    def __init__(self):
        self.env: str = "dev"
        self.settings: Settings = Settings()

    def load(self) -> str:
        self.env = os.getenv("FASTAPI_ENV", "dev")
        dotenv_file = f".env.{self.env}"
        load_dotenv(dotenv_file)
        self.settings = Settings()
        return self.settings
