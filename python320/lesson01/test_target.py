import pytest
from unittest import mock
import target
import queue

@mock.patch('target.temperature_sensor.read_temperature', mock.Mock(side_effect=(75, 10, -1)))
def test_get_current_temperature():
    expected_queue = queue.Queue()
    expected_queue.put("Nice temperature, 75F!")
    expected_queue.put("Tough weather, 10F")

    assert target.get_current_temperature() == expected_queue.get()
    assert target.get_current_temperature() == expected_queue.get()

    with pytest.raises(SystemError):
        target.get_current_temperature()

@mock.patch('target.temperature_sensor.convert_to')
def test_perform_conversion_C_to_F(mocked_function):
    mocked_function.return_value = 32
    result = target.perform_conversion(0, 'Fahrenheit')
    assert result == 'A reading of 0 degrees Celsius is equivalent to 32 degrees Fahrenheit'
    mocked_function.assert_called_with(0, 'Fahrenheit')

@mock.patch('target.temperature_sensor.convert_to')
def test_perform_conversion_F_to_C(mocked_function):
    mocked_function.return_value = 32
    result = target.perform_conversion(0, 'Celsius')
    assert result == 'A reading of 0 degrees Fahrenheit is equivalent to 32 degrees Celsius'
    mocked_function.assert_called_with(0, 'Celsius')
