'''
User related models module
'''

from tortoise import fields, models  # type: ignore
# from tortoise.contrib.pydantic import pydantic_model_creator  # type: ignore


class Users(models.Model):
    '''
    User model
    '''

    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=50, null=False)
    last_name = fields.CharField(max_length=100, null=False)
    password_hash = fields.CharField(max_length=128, null=True)
