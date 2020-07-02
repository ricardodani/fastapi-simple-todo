'''
List and Items tables repositories
'''

from typing import List as ListType

from app.models.todo import List, Item
from app.schemas.todo import ListSchema, ListInput, ItemSchema, ItemInput


class ListRepository:

    @classmethod
    async def create(cls, list_input: ListInput) -> ListSchema:
        list_obj = await List.create(**list_input.to_orm())
        return ListSchema.from_orm(list_obj)

    @classmethod
    async def check_list_exists(cls, list_id: int) -> bool:
        '''
        Checks if a given list existts
        '''
        return await List.filter(id=list_id).exists()

    @classmethod
    async def delete_list(cls, list_id: int):
        return await List.filter(id=list_id).delete()


class ItemRepository:

    @classmethod
    async def filter_by_list(cls, list_id: int) -> ListType[ItemSchema]:
        '''
        Return all items related to a list_id
        '''
        item_queryset = await Item.filter(list_id=list_id)
        return [
            ItemSchema.from_orm(item) for item in item_queryset
        ]

    @classmethod
    async def add_item(cls, list_id: int, item_input: ItemInput) -> ItemSchema:
        '''
        Adds a item to a given list
        '''
        item_data = {'list_id': list_id, **item_input.to_orm()}
        item_obj = await Item.create(**item_data)
        return ItemSchema.from_orm(item_obj)

    @classmethod
    async def delete_items(cls, list_id: int):
        return await Item.filter(list_id=list_id).delete()

    @classmethod
    async def check_item_exists(cls, list_id: int, item_id: int) -> bool:
        '''
        Checks if a given item exists
        '''
        return await Item.filter(id=item_id, list_id=list_id).exists()

    @classmethod
    async def edit_item(cls, list_id: int, item_id: int, item: ItemInput):
        await Item.filter(id=item_id, list_id=list_id).update(**item.to_orm())
