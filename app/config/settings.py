from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Mega AI"
    APP_VERSION: str = "1.0.0"

    API_HOST: str = "127.0.0.1"
    API_PORT: int = 8000

    DEBUG: bool = True

    DATABASE_URL: str 
    REDIS_URL: str
    OPENROUTER_API_KEY: str
    TAVILY_API_KEY: str
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )


settings = Settings()