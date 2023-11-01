from unittest import TestCase
import target

class TestTarget(TestCase):

    def setUp(self):
        self.control_value = "Some value"

    def tearDown(self):
        self.control_value = ""

    def test_addition(self):
        expected_output = 9
        result = target.addition(4,5)
        self.assertTrue(result == expected_output)
        self.assertTrue(self.control_value == "Some value")

    def test_addition_false(self):
        expected_output = 10
        result = target.addition(4,5)
        self.assertFalse(result == expected_output)
        self.assertTrue(self.control_value == "Some value")

    # This test will run first because of alphabetical order
    def test_aa_multiplication(self):
        self.control_value = "Another value"
        expected_output = 30
        result = target.multiplication(10,3)
        self.assertTrue(result == expected_output)
        self.assertTrue(self.control_value == "Another value")