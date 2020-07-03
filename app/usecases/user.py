import logging
from app.schemas.user import UserInput
from app.repositories.user import UserRepository
from app.usecases.exceptions import UseCaseValidationError
from app.core.security import get_password_hash


logger = logging.getLogger(__name__)


class UserUseCase:

    @classmethod
    async def register_user(cls, user_input: UserInput) -> None:
        '''
        Register a user in database, checking if it's valid first.

        Raises `UseCaseValidationError`
        '''
        if await UserRepository.check_user_exists(user_input.email):
            raise UseCaseValidationError('User with this email already exists')

        hashed_password = get_password_hash(user_input.password)
        logger.info(f"Adding {user_input!r} hashed_password={hashed_password}")
        await UserRepository.create(user_input, hashed_password)

    @classmethod
    async def authenticate_user(cls, email, password) -> bool:
        '''
        Check if there is a user with this `email` and `password`

        Raises `UseCaseValidationError`
        '''
        hashed_password = get_password_hash(password)
        logger.info(f"Auth email={email} hashed_password={hashed_password}")
        return await UserRepository.check_credentials_exists(
            email, hashed_password
        )
