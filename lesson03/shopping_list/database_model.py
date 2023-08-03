from peewee import *

#database = SqliteDatabase('shopping_list.db')
database = SqliteDatabase(':memory:')
database.connect()
# This line guarantees that foreign key dependencies will be enforced
# Not important for this example, but useful for the assignment
database.pragma('foreign_keys', 1, permanent=True)

class BaseModel(Model):
    class Meta:
        # Ties our database, created on line 3 with the "database" attribute in the Meta class
        database = database

class ShoppingListTable(BaseModel):
    product_code = CharField(primary_key=True, max_length=5)
    product_description = CharField(max_length=10)

database.create_tables([
    ShoppingListTable,
])

database.close()
