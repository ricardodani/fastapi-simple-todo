import hashlib
from base64 import b64encode
from fastapi import status, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials


http_security = HTTPBasic()


def get_password_hash(password: str) -> str:
    return hashlib.sha512(password.encode()).hexdigest()


def get_auth_header(username: str, password: str) -> dict:
    basic_token = b64encode(f"{username}:{password}".encode()).decode()
    return dict(Authorization=f"Basic {basic_token}")


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
