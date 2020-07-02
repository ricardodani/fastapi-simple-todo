from app.schemas.user import UserInput
from app.repositories.user import UserRepository
from app.usecases.exceptions import UseCaseValidationError


class UserUseCase:

    @classmethod
    async def register_user(cls, user_input: UserInput) -> None:
        '''
        Register a user in database, checking if it's valid first.

        Raises `ValidationError`
        '''
        if await UserRepository.check_user_exists(user_input.email):
            raise UseCaseValidationError('User with this email already exists')

        await UserRepository.create(user_input)
