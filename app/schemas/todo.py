from pydantic import BaseModel

class ListInput(BaseModel):
    list_name: str


class ListSchema(ListInput):
    list_id: int


class ItemInput(BaseModel):
    todo_item_name: str


class ItemSchema(ItemInput):
    todo_item_id: int
