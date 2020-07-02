from typing import List as ListType

from tortoise.transactions import in_transaction  # type: ignore

from app.schemas.todo import ListInput, ListSchema, ItemSchema, ItemInput
from app.repositories.todo import ListRepository, ItemRepository
from app.usecases.exceptions import UseCaseValidationError


class ListUseCase:

    @classmethod
    async def create_list(cls, list_input: ListInput) -> ListSchema:
        '''
        Register a TODO list in database and return it with it's id.
        '''
        return await ListRepository.create(list_input)

    @classmethod
    async def view_list(cls, list_id: int) -> ListType[ItemSchema]:
        '''
        Return a list of items related to a `list_id` list if the list exists.
        '''
        if not await ListRepository.check_list_exists(list_id):
            raise UseCaseValidationError('List does not exists')
        return await ItemRepository.filter_by_list(list_id)

    @classmethod
    async def delete_list(cls, list_id: int) -> None:
        '''
        Remove a list and it's items if list exists
        '''
        if not await ListRepository.check_list_exists(list_id):
            raise UseCaseValidationError('List does not exists')
        async with in_transaction():  # TODO: should be in repository?!
            await ItemRepository.delete_items(list_id)
            await ListRepository.delete_list(list_id)

    @classmethod
    async def add_item(cls, list_id: int, item: ItemInput) -> ItemSchema:
        '''
        Add a item to a list givin its `list_id`
        '''
        if not await ListRepository.check_list_exists(list_id):
            raise UseCaseValidationError('List does not exists')
        return await ItemRepository.add_item(list_id, item)

    @classmethod
    async def edit_item(cls, list_id: int, item_id: int, item: ItemInput):
        '''
        Edit a specific item of a list given its list and item ids if it exists
        '''
        if not await ItemRepository.check_item_exists(list_id, item_id):
            raise UseCaseValidationError('List Item does not exists')
        return await ItemRepository.edit_item(list_id, item_id, item)

    @classmethod
    async def delete_item(cls, list_id: int, item_id: int):
        '''
        Deletes a specific item of a list given its list and item ids if exists
        '''
        if not await ItemRepository.check_item_exists(list_id, item_id):
            raise UseCaseValidationError('List Item does not exists')
        await ItemRepository.delete_item(list_id, item_id)
