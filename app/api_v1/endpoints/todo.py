'''
Endpoints definition from api v1
'''

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasicCredentials

from app.schemas.todo import ListInput, ListSchema, ItemInput, ItemSchema
from app.usecases.todo import ListUseCase
from app.usecases.exceptions import UseCaseValidationError
from app.core.security import authenticate


router = APIRouter()


@router.post("/list", response_model=ListSchema)
async def create_list(
    list_input: ListInput,
    credentials: HTTPBasicCredentials = Depends(authenticate)
):
    '''
    Creates a list endpoint
    '''
    return await ListUseCase.create_list(list_input)


@router.get("/list/{list_id}", response_model=List[ItemSchema])
async def view_list(
    list_id: int,
    credentials: HTTPBasicCredentials = Depends(authenticate)
):
    '''
    View a list by its `list_id` endpoint
    '''
    try:
        return await ListUseCase.view_list(list_id)
    except UseCaseValidationError as error:  # todo, use a notfound here
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error)
        )


@router.delete("/list/{list_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_list(
    list_id: int,
    credentials: HTTPBasicCredentials = Depends(authenticate)
):
    '''
    Delete a `list_id` list endpoint
    '''
    try:
        return await ListUseCase.delete_list(list_id)
    except UseCaseValidationError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error)
        )


@router.post("/list/{list_id}", response_model=ItemSchema)
async def add_item(
    list_id: int, item: ItemInput,
    credentials: HTTPBasicCredentials = Depends(authenticate)
):
    '''
    Adds a item to a list of a `list_id` endpoint
    '''
    try:
        return await ListUseCase.add_item(list_id, item)
    except UseCaseValidationError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error)
        )


@router.put(
    "/list/{list_id}/{item_id}", status_code=status.HTTP_204_NO_CONTENT
)
async def update_item(
    list_id: int, item_id: int, item: ItemInput,
    credentials: HTTPBasicCredentials = Depends(authenticate)
):
    '''
    Updates a item `item_id` of a given list `id` endpoint
    '''
    try:
        return await ListUseCase.edit_item(list_id, item_id, item)
    except UseCaseValidationError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error)
        )


@router.delete(
    "/list/{list_id}/{item_id}", status_code=status.HTTP_204_NO_CONTENT
)
async def delete_item(
    list_id: int, item_id: int,
    credentials: HTTPBasicCredentials = Depends(authenticate)
):
    '''
    Deletes given item `item_id` of a given list `id` endpoint
    '''
    try:
        return await ListUseCase.delete_item(list_id, item_id)
    except UseCaseValidationError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error)
        )
