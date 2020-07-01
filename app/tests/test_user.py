'''
TODO app test cases
'''

import asyncio

from fastapi.testclient import TestClient

from app.models.user import Users
from app.tests.fixtures import client, event_loop  # noqa: dependency injection


def test_register_user(client: TestClient, event_loop: asyncio.AbstractEventLoop): # noqa: dependency injection
    '''
    Test registering a user
    '''
    response = client.post("/api/v1/users", json={"username": "admin"})
    assert response.status_code == 200, response.text
    data = response.json()
    assert data['username'] == "admin"
    assert "id" in data
    user_id = data["id"]

    async def get_user_by_db():
        user = await Users.get(id=user_id)
        return user

    user_obj = event_loop.run_until_complete(get_user_by_db())
    assert user_obj.id == user_id
