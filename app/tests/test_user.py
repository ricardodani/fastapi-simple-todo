'''
TODO user test cases
'''

import asyncio

from fastapi import status
from fastapi.testclient import TestClient
from requests.auth import HTTPBasicAuth

from app.tests.fixtures import client, event_loop  # noqa: F401
from app.schemas.user import UserInput
from app.repositories.user import UserRepository
from app.usecases.user import UserUseCase
from app.core.config import settings
# from app.core.security import get_auth_header


def get_url(path: str) -> str:
    return f"{settings.API_V1_STR}{path}"


def test_register_user(
    client: TestClient, event_loop: asyncio.AbstractEventLoop  # noqa: F811
):
    '''
    Test registering a user
    '''
    url = get_url("/register")
    user_input = UserInput(
        email="email@email.com", first_name="F", last_name="L", password="123"
    )

    response = client.post(url, json=user_input.dict())
    assert response.status_code == status.HTTP_204_NO_CONTENT

    async def check_user():
        return await UserRepository.check_user_exists(user_input.email)
    assert event_loop.run_until_complete(check_user())


def test_read_current_user(
    client: TestClient, event_loop: asyncio.AbstractEventLoop  # noqa: F811
):
    '''
    Test a registerd user reading it's authenticated credentials
    '''

    user_input = UserInput(
        email="email2@email.com", first_name="F", last_name="L", password="123"
    )
    async def add_user():
        return await UserUseCase.register_user(user_input)
    event_loop.run_until_complete(add_user())

    url = get_url("/__user__")
    basic_auth = HTTPBasicAuth(
        username=user_input.email, password=user_input.password
    )
    response = client.get(url, auth=basic_auth)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == user_input.email
