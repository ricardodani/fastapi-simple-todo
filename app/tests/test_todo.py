'''
TODO list and item test cases
'''

import asyncio

from fastapi import status
from fastapi.testclient import TestClient

from app.tests.fixtures import client, event_loop  # noqa: F401
from app.schemas.todo import ListInput, ItemInput
from app.repositories.todo import ListRepository, ItemRepository
from app.core.config import settings


def get_url(path: str) -> str:
    return f"{settings.API_V1_STR}{path}"


def test_create_list(client: TestClient):  # noqa: F811
    '''
    Test creating a TODO list endpoint
    '''
    url = get_url("/list")
    list_input = ListInput(list_name="List A")

    response = client.post(url, json=list_input.dict())
    assert response.status_code == status.HTTP_200_OK

    r_user = response.json()
    assert r_user
    assert r_user["list_name"] == list_input.list_name
    assert isinstance(r_user["list_id"], int)


def test_view_list(
    client: TestClient, event_loop: asyncio.AbstractEventLoop  # noqa: F811
):
    '''
    Test viewing items of a list endpoint
    '''
    # invalid list
    url = get_url("/list/0")
    response = client.get(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND

    # empty list
    async def create_empty_list():
        list_input = ListInput(list_name="List A")
        return await ListRepository.create(list_input)
    created_list = event_loop.run_until_complete(create_empty_list())
    url = get_url(f"/list/{created_list.list_id}")
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    r_items = response.json()
    assert r_items == []

    # list with items
    async def add_items_to_list():
        item_a = await ItemRepository.add_item(
            created_list.list_id, ItemInput(todo_item_name="Item A")
        )
        item_b = await ItemRepository.add_item(
            created_list.list_id, ItemInput(todo_item_name="Item B")
        )
        return item_a, item_b
    item_a, item_b = event_loop.run_until_complete(add_items_to_list())
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    r_items = response.json()
    assert r_items[0]['todo_item_name'] == item_a.todo_item_name
    assert r_items[1]['todo_item_id'] == item_b.todo_item_id


def test_delete_list(
    client: TestClient, event_loop: asyncio.AbstractEventLoop  # noqa: F811
):
    '''
    Test deleting a list
    '''
    # invalid list
    url = get_url("/list/0")
    response = client.delete(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND

    # empty list
    async def create_empty_list():
        list_input = ListInput(list_name="List A")
        return await ListRepository.create(list_input)
    created_list = event_loop.run_until_complete(create_empty_list())
    url = get_url(f"/list/{created_list.list_id}")
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT

    # recreating a list with an item
    created_list = event_loop.run_until_complete(create_empty_list())
    url = get_url(f"/list/{created_list.list_id}")

    async def add_item_to_list():
        await ItemRepository.add_item(
            created_list.list_id, ItemInput(todo_item_name="Item A")
        )
    event_loop.run_until_complete(add_item_to_list())
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_add_to_list(
    client: TestClient, event_loop: asyncio.AbstractEventLoop  # noqa: F811
):
    '''
    Testing adding a item to a list endpoint
    '''

    # invalid list
    url = get_url("/list/0")
    item = ItemInput(todo_item_name="Item A")
    response = client.post(url, json=item.dict())
    assert response.status_code == status.HTTP_404_NOT_FOUND

    # empty list
    async def create_empty_list():
        list_input = ListInput(list_name="List A")
        return await ListRepository.create(list_input)
    created_list = event_loop.run_until_complete(create_empty_list())
    url = get_url(f"/list/{created_list.list_id}")
    response = client.post(url, json=item.dict())
    assert response.status_code == status.HTTP_200_OK
    item_response = response.json()
    assert item_response['todo_item_name']
    assert item_response['todo_item_id']

    async def check_item_exists():
        return await ItemRepository.check_item_exists(
            created_list.list_id,
            item_response['todo_item_id']
        )
    assert event_loop.run_until_complete(check_item_exists())


def test_edit_item_list(
    client: TestClient, event_loop: asyncio.AbstractEventLoop  # noqa: F811
):
    '''
    Testing editing a item of a list
    '''

    # invalid item
    url = get_url("/list/0/0")
    item_a = ItemInput(todo_item_name="Item A")
    response = client.put(url, json=item_a.dict())
    assert response.status_code == status.HTTP_404_NOT_FOUND

    # list with item
    async def create_list_with_item():
        list_input = ListInput(list_name="List A")
        item_b = ItemInput(todo_item_name="Item B")
        created_list = await ListRepository.create(list_input)
        created_item = await ItemRepository.add_item(
            created_list.list_id, item_b
        )
        return created_list, created_item
    created_list, created_item = event_loop.run_until_complete(
        create_list_with_item()
    )
    url = get_url(f"/list/{created_list.list_id}/{created_item.todo_item_id}")
    response = client.put(url, json=item_a.dict())
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_delete_item_list(
    client: TestClient, event_loop: asyncio.AbstractEventLoop  # noqa: F811
):
    '''
    Testing deleting a item of a list
    '''

    # invalid item
    url = get_url("/list/0/0")
    item_a = ItemInput(todo_item_name="Item A")
    response = client.delete(url, json=item_a.dict())
    assert response.status_code == status.HTTP_404_NOT_FOUND

    # list with item
    async def create_list_with_item():
        list_input = ListInput(list_name="List A")
        item_b = ItemInput(todo_item_name="Item B")
        created_list = await ListRepository.create(list_input)
        created_item = await ItemRepository.add_item(
            created_list.list_id, item_b
        )
        return created_list, created_item
    created_list, created_item = event_loop.run_until_complete(
        create_list_with_item()
    )
    url = get_url(f"/list/{created_list.list_id}/{created_item.todo_item_id}")
    response = client.delete(url, json=item_a.dict())
    assert response.status_code == status.HTTP_204_NO_CONTENT

    async def check_item_exists():
        return await ItemRepository.check_item_exists(
            created_list.list_id,
            created_item.todo_item_id
        )
    assert not event_loop.run_until_complete(check_item_exists())
