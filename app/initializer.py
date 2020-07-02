'''
Todo app initialization hooks
'''

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise  # type: ignore

from app.api_v1.api import api_router
from app.core.config import settings, tortoise_settings


def _init_db(app: FastAPI):
    '''
    Initializes the database
    '''
    register_tortoise(
        app,
        db_url=tortoise_settings.db_url,
        generate_schemas=tortoise_settings.generate_schemas,
        modules=tortoise_settings.modules
    )


def _init_routers(app: FastAPI):
    '''
    Initializes the API endpoints
    '''
    app.include_router(api_router, prefix=settings.API_V1_STR)


def init_app(app: FastAPI):
    '''
    Init app main method
    '''
    _init_db(app)
    _init_routers(app)

