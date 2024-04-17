import os

from peewee import Model, CharField, IntegerField
from playhouse.db_url import connect

db = connect(os.environ.get('DATABASE_URL', 'sqlite:///my_database.db'))

class SavedTotal(Model):
    code = CharField(max_length=255, unique=True)
    value = IntegerField()

    class Meta:
        database = db