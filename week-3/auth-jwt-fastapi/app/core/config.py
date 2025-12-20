from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Authentication JWT"
    DEBUG: bool = True

    # Database Settings
    SQLALCHEMY_DATABASE_URI: Optional[str] = None
    POSTGRES_USER: Optional[str] = None
    POSTGRES_PASSWORD: Optional[str] = None
    POSTGRES_SERVER: Optional[str] = None
    POSTGRES_PORT: Optional[str] = None
    POSTGRES_DB: Optional[str] = None

    if SQLALCHEMY_DATABASE_URI is None:
        SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    
    # JWT Settings
    SECRET_KEY: Optional[str] = "dummy-secret-key-keep-it-secret"
    ALGORITHM: Optional[str] = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: Optional[int] = 60 * 24 * 7
    
    # CORS Settings
    BACKEND_CORS_ORIGINS: list[str] = ["*"]
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()