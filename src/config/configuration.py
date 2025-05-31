from src.model import DatabaseConfig
from src.config.settings import DATABASE_DEV


def get_database_config() -> DatabaseConfig:
    return DATABASE_DEV
