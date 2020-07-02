'''
Todo list related models
'''

from tortoise import fields, models  # type: ignore


class List(models.Model):
    '''
    List model
    '''

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100, null=False)


class Item(models.Model):
    '''
    Item of a list model
    '''
    id = fields.IntField(pk=True)
    list = fields.ForeignKeyField('models.List', related_name='items')
    name = fields.CharField(max_length=100, null=False)
