'''
API v1 base router definition
'''

from fastapi import APIRouter


from app.api_v1.endpoints import router


api_router = APIRouter()
api_router.include_router(router, prefix="/v1", tags=["api"])
