'''
API v1 base router definition
'''

from fastapi import APIRouter


from app.api_v1.endpoints.user import router as user_router
from app.api_v1.endpoints.todo import router as todo_router


api_router = APIRouter()
api_router.include_router(user_router)
api_router.include_router(todo_router)
