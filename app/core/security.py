import hashlib
from fastapi import status, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials


http_security = HTTPBasic()


def get_password_hash(password: str) -> str:
    return hashlib.sha512(password.encode()).hexdigest()


async def authenticate(
    credentials: HTTPBasicCredentials = Depends(http_security)
) -> str:
    from app.usecases.user import UserUseCase
    if not await UserUseCase.authenticate_user(
        credentials.username, credentials.password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
