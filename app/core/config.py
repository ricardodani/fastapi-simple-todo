'''
App`s config module
'''

from pydantic import BaseSettings
from .db import TortoiseSettings


PROJECT_NAME = "TODO List API"


class Settings(BaseSettings):
    '''
    Project settings base definition
    '''
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = PROJECT_NAME
    DEBUG: bool = True


settings = Settings()
tortoise_settings = TortoiseSettings.generate(
    test_db=settings.DEBUG
)
