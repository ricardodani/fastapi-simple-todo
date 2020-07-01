
from typing import List
from fastapi import APIRouter, HTTPException, status
from app.schemas.user import UserInput
from app.schemas.todo import ListInput, ListSchema, ItemInput, ItemSchema


router = APIRouter()


@router.post("/register", status_code=status.HTTP_204_NO_CONTENT)
def register_user(user_input: UserInput):
    '''
    Registers a User
    '''
    raise HTTPException(
        status_code=400,
        detail="User already exists"
    )

@router.post("/list", response_model=ListSchema)
def create_list(list_input: ListInput):
    '''
    Creates a list
    '''
    if 1 == False:
        raise HTTPException(status_code=400)
    return ListSchema(list_id=1, list_name="Ricardo")


@router.get("/list/{list_id}", response_model=List[ListSchema])
def view_list(list_id: int):
    '''
    View a list by its `list_id`
    '''
    return [ListSchema(list_id=1, list_name="bla")]


@router.delete("/list/{list_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_list(list_id: int):
    '''
    Delete a `list_id` list
    '''
    pass


@router.post("/list/{list_id}", response_model=ItemSchema)
def add_item(list_id: int, item: ItemInput):
    '''
    Adds a item to a list of a `list_id`
    '''
    return ItemSchema(todo_item_name="Bla", todo_item_id=1)


@router.put("/list/{id}/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def update_item(id: int, item_id: int, item: ItemInput):
    '''
    Updates a item `item_id` of a given list `id`
    '''
    pass


@router.delete("/list/{id}/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(id: int, item_id: int):
    '''
    Deletes given item `item_id` of a given list `id`
    '''
    pass
