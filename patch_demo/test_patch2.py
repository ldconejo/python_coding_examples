from unittest import TestCase
from mock import Mock, patch
import patch_tutorial2 as PT2
import queue

class TestPatchTutorial2(TestCase):
    def test_get_current_temperature(self):
        responses = (75, 10, -1)
        expected_queue = queue.Queue()
        expected_queue.put("Nice temperature, 75F!")
        expected_queue.put("Tough weather, 10F")

        with patch('patch_tutorial2.temperature_sensor.read_temperature', side_effect=responses):
            self.assertEqual(PT2.get_current_temperature(), expected_queue.get())
            self.assertEqual(PT2.get_current_temperature(), expected_queue.get())
            self.assertRaises(SystemError, PT2.get_current_temperature)

            #with self.assertRaises(SystemError):
            #    PT2.get_current_temperature()