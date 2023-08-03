from unittest import TestCase
from database_model import database, ShoppingListTable

import shopping_list

class TestSocialNetwork(TestCase):
    def setUp(self):
        database.connect()
        database.pragma('foreign_keys', 1, permanent=True)
        database.create_tables([
            ShoppingListTable,
        ])
        self.shopping_list_instance = shopping_list.ShoppingListCollection(database)
        item_id = 'generic01'
        item_description = 'Just a generic item'
        self.shopping_list_instance.add_item(item_id, item_description)

    def tearDown(self):
        database.drop_tables([
            ShoppingListTable,
        ])
        database.close()

    def test_add_item_true(self):
        self.assertTrue(self.shopping_list_instance.add_item('generic02', 'Another item'))

    def test_add_item_false(self):
        self.assertFalse(self.shopping_list_instance.add_item('generic01', 'Some description'))

    def test_update_item_true(self):
        self.assertTrue(self.shopping_list_instance.update_item('generic01', 'updated description'))
        result = self.shopping_list_instance.search_item('generic01')
        self.assertEqual(result.product_description, 'updated description')

    def test_update_item_false(self):
        self.assertFalse(self.shopping_list_instance.update_item('false01', 'updated description'))

    def test_delete_item_true(self):
        self.assertTrue(self.shopping_list_instance.delete_item('generic01'))

    def test_delete_item_false(self):
        self.assertFalse(self.shopping_list_instance.delete_item('something01'))

    def test_search_item_success(self):
        result = self.shopping_list_instance.search_item('generic01')
        self.assertEqual(result.product_description, 'Just a generic item')

    def test_search_item_fail(self):
        self.assertIsNone(self.shopping_list_instance.search_item('something02'))
