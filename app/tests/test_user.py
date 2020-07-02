'''
TODO user test cases
'''

import asyncio

from fastapi import status
from fastapi.testclient import TestClient

from app.tests.fixtures import client, event_loop  # noqa: dependency injection
from app.schemas.user import UserInput
from app.repositories.user import UserRepository
from app.core.config import settings


def get_url(path: str) -> str:
    return f"{settings.API_V1_STR}{path}"


def test_register_user(client: TestClient, event_loop: asyncio.AbstractEventLoop): # noqa: dependency injection
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
