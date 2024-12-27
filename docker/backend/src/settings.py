import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = os.environ['APP_NAME']
    APP_VERSION: str = os.environ['APP_VERSION']
    DEBUG: bool = os.environ['DEBUG']

class Auth(BaseSettings):
    SECRET_KEY: str = os.environ['SECRET_KEY']
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

class DataBase(BaseSettings):
    POSTGRESQL_HOSTNAME: str = os.environ['POSTGRES_HOST']
    POSTGRESQL_HOSTNAME_DOCKER: str = os.environ['POSTGRES_HOST_DOCKER']
    POSTGRESQL_USERNAME: str = os.environ['POSTGRES_USER']
    POSTGRESQL_PASSWORD: str = os.environ['POSTGRES_PASSWORD']
    POSTGRESQL_DATABASE: str = os.environ['POSTGRES_DB']

SETTINGS = Settings()
AUTH = Auth()
DATABASE = DataBase()