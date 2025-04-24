from app.app_dependency import get_env_service
from app.app_factory import create_app

env = get_env_service()
settings = env.load()
app = create_app(settings=settings)
