'''
TODO List main app module

Author: @ricardodani
'''

from fastapi import FastAPI
from app.core.config import settings
from app.api_v1.api import api_router

app = FastAPI(
    title=settings.PROJECT_NAME
)

app.include_router(api_router, prefix=settings.API_V1_STR)
