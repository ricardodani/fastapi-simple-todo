'''
TODO List main app module

Author: @ricardodani
'''

from fastapi import FastAPI
from app.core.config import settings
from app.initializer import init_app


app = FastAPI(
    title=settings.PROJECT_NAME
)
init_app(app)
