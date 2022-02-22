from unittest import TestCase
from mock import Mock
import mock_tutorial as MT

class TutorialTests(TestCase):
    def test_get_user_info(self):
        MT.input = Mock(return_value = 'Luis')
        self.assertEqual(MT.get_user_info(), 'Luis')

    def test_get_current_temperature_nice(self):
        MT.temperature_sensor.read_temperature = Mock(return_value = 75)
        expected_response = 'Nice temperature, 75F!'
        self.assertEqual(MT.get_current_temperature(), expected_response)

    def test_get_current_temperature_bad(self):
        MT.temperature_sensor.read_temperature = Mock(return_value = 28)
        expected_response = 'Tough weather, 28F'
        self.assertEqual(MT.get_current_temperature(), expected_response)

    def test_get_current_temperature_below_zero(self):
        MT.temperature_sensor.read_temperature = Mock(return_value = -10)
        self.assertRaises(SystemError, MT.get_current_temperature)