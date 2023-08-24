from peewee import IntegrityError, DoesNotExist
from database_model import ShoppingListTable

class ShoppingListCollection():

    def __init__(self, shopping_database):
        self.database = shopping_database

    def add_item(self, item_id, item_description):
        with self.database.transaction():
            try:
                new_item = ShoppingListTable.create(
                    product_code = item_id,
                    product_description = item_description
                )
                new_item.save()
                return True
            except IntegrityError:
                return False
            
    def update_item(self, item_id, item_description):
        with self.database.transaction():
            try:
                # This line will pull the matching row, if it exists
                # and raise an exception if it doesn't
                modify_target = ShoppingListTable.get(ShoppingListTable.product_code == item_id)
                modify_target.product_description = item_description
                modify_target.save()
                return True
            except DoesNotExist:
                return False
            
    def delete_item(self, item_id):
        with self.database.transaction():
            try:
                delete_target = ShoppingListTable.get(ShoppingListTable.product_code == item_id)
                delete_target.delete_instance()
                return True
            except DoesNotExist:
                return False
            
    def search_item(self, item_id):
        with self.database.transaction():
            try:
                search_target = ShoppingListTable.get(ShoppingListTable.product_code == item_id)
            except DoesNotExist:
                search_target = None
            return search_target        
    