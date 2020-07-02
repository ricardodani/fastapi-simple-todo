'''
Todo list schemas
'''

from pydantic import BaseModel


class ListInput(BaseModel):
    '''
    List model for input data
    '''
    list_name: str

    def to_orm(self):
        return dict(name=self.list_name)


class ListSchema(ListInput):
    '''
    List model to represent data from base
    '''
    list_id: int

    @classmethod
    def from_orm(cls, orm_obj):
        return cls(list_id=orm_obj.id, list_name=orm_obj.name)


class ItemInput(BaseModel):
    '''
    Item model for input data
    '''
    todo_item_name: str

    def to_orm(self):
        return dict(name=self.todo_item_name)


class ItemSchema(ItemInput):
    '''
    Item model to represent data from base
    '''
    todo_item_id: int

    @classmethod
    def from_orm(cls, obj):
        return cls(todo_item_id=obj.id, todo_item_name=obj.name)
