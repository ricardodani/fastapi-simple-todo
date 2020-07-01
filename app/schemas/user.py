'''
User schemas
'''

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    '''
    User basic model
    '''
    email: EmailStr
    first_name: str
    last_name: str


class UserInput(UserBase):
    '''
    User input model
    '''
    password: str
