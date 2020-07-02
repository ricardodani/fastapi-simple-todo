'''
User endpoints definition from api v1
'''

from fastapi import APIRouter, HTTPException, status

from app.schemas.user import UserInput
from app.usecases.user import UserUseCase
from app.usecases.exceptions import UseCaseValidationError

router = APIRouter()


@router.post("/register", status_code=status.HTTP_204_NO_CONTENT)
async def register_user(user_input: UserInput):
    '''
    Registers a User endpoint
    '''
    try:
        await UserUseCase.register_user(user_input)
    except UseCaseValidationError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )
