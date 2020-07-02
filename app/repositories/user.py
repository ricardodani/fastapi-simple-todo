'''
User table repository
'''

from typing import Optional
from tortoise.queryset import DoesNotExist  # type: ignore
from tortoise.transactions import in_transaction  # type: ignore

from app.core.security import get_password_hash, verify_password
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
        hashed_password = get_password_hash(user_input.password)
        async with in_transaction():
            await User.create(
                email=user_input.email,
                first_name=user_input.first_name,
                last_name=user_input.last_name,
                password_hash=hashed_password
            )

    @classmethod
    async def authenticate(cls, email: str, password: str) -> Optional[User]:
        try:
            user = await User.get(email=email)
        except DoesNotExist:
            return None
        else:
            if not verify_password(password, user.hashed_password):
                return None
            else:
                return user
