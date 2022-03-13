from unittest import TestCase
import target

class MainTest(TestCase):
    def setUp(self):
        pass

    def test_display_user_data_pass(self):
        self.assertTrue(target.display_user_data('pass.csv'))

    def test_display_user_data_file_not_found(self):
        self.assertFalse(target.display_user_data('missing.csv'))

    def test_display_user_data_file_empty_fields(self):
        self.assertFalse(target.display_user_data('fail.csv'))
        self.assertFalse(target.display_user_data('fail2.csv'))