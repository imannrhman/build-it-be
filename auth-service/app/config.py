from pydantic import BaseSettings


class Settings(BaseSettings):
    DEFAULT_VARIABLE: str = "default value"
    SECRET_KEY: str
    SECRET_REFRESH_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: str
    REFRESH_TOKEN_EXPIRE_MINUTES: str

    class Config:
        env_file = ".env"
