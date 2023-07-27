from unittest import TestCase
from unittest.mock import mock_open, patch
import example
import os

class MainTest(TestCase):
    def setUp(self):
        self.expected_items = [
            {
                'item_name': 'Orange juice',
                'item_price': '5.99'
            },
            {
                'item_name': 'Eggs',
                'item_price': '7.99'
            }
        ]
        self.filename = 'test_invoice.csv'

    def tearDown(self):
        os.remove(self.filename)

    def test_interact_with_user(self):
        '''
        Tests user interface
        '''
        user_responses = (self.filename, 'Orange juice', '5.99', 'y', 'Eggs', '7.99', 'n')
        expected_filename = 'test_invoice.csv'

        with patch('builtins.input', side_effect=user_responses):
            result_filename, result_items = example.interact_with_user()
            self.assertEqual(result_filename, expected_filename)
            self.assertEqual(result_items, self.expected_items)

    def test_save_file(self):
        ''''
        Tests the save file function
        '''

        #with patch('example.open', mock_open()):
        self.assertTrue(example.save_file(self.filename, self.expected_items))