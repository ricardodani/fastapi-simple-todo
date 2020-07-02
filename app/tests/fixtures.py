'''
TODO app test fixtures
'''

from typing import Generator

import pytest  # type: ignore
from fastapi.testclient import TestClient
from tortoise.contrib.test import finalizer, initializer  # type: ignore

from app.main import app


@pytest.fixture(scope="module")
def client() -> Generator:
    '''
    Generates a TestClient instance for models.user
    '''
    initializer(["app.models"])
    with TestClient(app) as test_client:
        yield test_client
    finalizer()


@pytest.fixture(scope="module")
def event_loop(client: TestClient) -> Generator:
    '''
    Generates a event loop to run async methods
    '''
    yield client.task.get_loop()
