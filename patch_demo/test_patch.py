from unittest import TestCase
from mock import Mock, patch
import patch_tutorial as PT

class TestPatchTutorial(TestCase):

    def test_get_user_input_human(self):
        responses = ('Luis', 'Conejo', '40', 'n')
        expected = "You are Luis Conejo, and you're 40 years old."

        with patch('builtins.input', side_effect=responses):
            self.assertEqual(PT.get_user_input(), expected)

    def test_get_user_input_robot(self):
        responses = ('Daneel', 'Olivaw', '19230', 'y')
        expected = "Welcome, my artificial friend!"

        with patch('builtins.input', side_effect=responses):
            self.assertEqual(PT.get_user_input(), expected)

    def test_get_user_input_other(self):
        responses = ('Nubi', 'Hamster', '1', 'neither')
        expected = "You are not a human or a robot. What are you?"

        with patch('builtins.input', side_effect=responses):
            self.assertEqual(PT.get_user_input(), expected)