from os import path
from unittest import TestCase
from unittest.mock import Mock, patch, mock_open
import target

class MainTest(TestCase):
    def setUp(self):
        self.csv_dict_reader_backup = target.csv.DictReader

    def tearDown(self):
        target.csv.DictReader = self.csv_dict_reader_backup

    def test_display_user_data_pass(self):
        with patch('target.open', mock_open()):
            good_file = iter([{
                'name': 'Luis',
                'last_name': 'Conejo',
                'position': 'Instructor'
            },])
            target.csv.DictReader = Mock(return_value=good_file)
            self.assertTrue(target.display_user_data('some.csv'))

    def test_display_user_data_file_not_found(self):
        with patch('target.open', mock_open()) as mocked_open:
            mocked_open.side_effect = FileNotFoundError()
            self.assertFalse(target.display_user_data(''))

    def test_display_user_data_file_os_error(self):
        with patch('target.open', mock_open()) as mocked_open:
            mocked_open.side_effect = OSError()
            self.assertFalse(target.display_user_data('some.csv'))

    def test_display_user_data_file_empty_fields(self):
        with patch('target.open', mock_open()):
            bad_file = iter([{
                'name': 'Luis',
                'last_name': '',
                'position': 'Instructor'
            },])
            target.csv.DictReader = Mock(return_value=bad_file)
            self.assertFalse(target.display_user_data('some.csv'))

            bad_file = iter([{
                'name': 'Luis',
                'last_name': 'Conejo',
                'position': '     '
            },])
            target.csv.DictReader = Mock(return_value=bad_file)
            self.assertFalse(target.display_user_data('some.csv'))
    