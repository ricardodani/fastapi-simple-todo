'''
User table repository
'''

from app.schemas.user import UserInput
from app.models.user import User


class UserRepository:

    @classmethod
    async def check_user_exists(cls, email: str) -> bool:
        '''
        Returns if exists a user
        '''
        return await User.filter(email=email).exists()

    @classmethod
    async def check_credentials_exists(
        cls, email: str, hashed_password: str
    ) -> bool:
        '''
        Returns if exists a user with this credentials
        '''
        return await User.filter(
            email=email, password_hash=hashed_password
        ).exists()

    @classmethod
    async def create(cls, user_input: UserInput, hashed_password: str) -> None:
        '''
        Creates a user base on user input
        '''
        await User.create(
            email=user_input.email,
            first_name=user_input.first_name,
            last_name=user_input.last_name,
            password_hash=hashed_password
        )
