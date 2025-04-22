from pydantic_settings import BaseSettings

class Environment(BaseSettings):
    PROJECT_NAME: str = "EYR App"
    DATABASE_URL: str = "sqlite:///./test.db"
    SECRET_KEY: str = "supersecret"

    class Config:
        env_file = ".env"

encironment = Environment()
