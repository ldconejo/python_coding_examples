from peewee import *

database = SqliteDatabase('database_model.db')
database.connect()
database.pragma('foreign_keys', 1, permanent=True)

class BaseModel(Model):
    """
        BaseModel class
    """
    class Meta:
        """
            Meta class
        """
        database = database

class DirectorsTable(BaseModel):
    """
        Table for user accounts.
    """
    director_id = CharField(primary_key=True, max_length=30)
    full_name = CharField(max_length=100)

class MoviesTable(BaseModel):
    """
        Table for status updates
    """
    movie_id = CharField(primary_key=True, max_length=100)
    director_id = ForeignKeyField(DirectorsTable, on_delete='CASCADE')
    movie_title = CharField(max_length=200)

# Creation of the database
database.create_tables([
        DirectorsTable,
        MoviesTable
    ])

database.close()