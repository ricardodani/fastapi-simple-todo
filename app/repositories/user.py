'''
User table repository
'''

from tortoise.queryset import DoesNotExist  # type: ignore
from tortoise.transactions import in_transaction  # type: ignore

from app.schemas.user import UserInput
from app.models.user import User


class UserRepository:

    @classmethod
    async def check_user_exists(cls, email: str) -> bool:
        '''
        Returns a `bool` if exists a user if this `email`
        '''
        try:
            await User.get(email=email)
        except DoesNotExist:
            return False
        else:
            return True

    @classmethod
    async def create(cls, user_input: UserInput) -> None:
        '''
        Creates a user base on a `UserInput`
        '''
        async with in_transaction():
            await User.create(
                **user_input.dict()
            )
