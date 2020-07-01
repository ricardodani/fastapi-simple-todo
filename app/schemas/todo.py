'''
Todo list schemas
'''

from pydantic import BaseModel


class ListInput(BaseModel):
    '''
    List model for input data
    '''
    list_name: str


class ListSchema(ListInput):
    '''
    List model to represent data from base
    '''
    list_id: int


class ItemInput(BaseModel):
    '''
    Item model for input data
    '''
    todo_item_name: str


class ItemSchema(ItemInput):
    '''
    Item model to represent data from base
    '''
    todo_item_id: int
