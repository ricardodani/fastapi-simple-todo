from pydantic import BaseSettings


PROJECT_NAME = "TODO List API"


class Settings(BaseSettings):
    API_V1_STR: str = "/api"
    PROJECT_NAME: str = PROJECT_NAME


settings = Settings()
