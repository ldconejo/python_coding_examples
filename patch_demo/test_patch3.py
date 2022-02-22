import pytest
import mock
import patch_tutorial2 as PT2
import queue

@mock.patch('patch_tutorial2.temperature_sensor.read_temperature', mock.Mock(side_effect=(75, 10, -1)))
def test_get_current_temperature():
    expected_queue = queue.Queue()
    expected_queue.put("Nice temperature, 75F!")
    expected_queue.put("Tough weather, 10F")

    assert PT2.get_current_temperature() == expected_queue.get()
    assert PT2.get_current_temperature() == expected_queue.get()

    with pytest.raises(SystemError):
        PT2.get_current_temperature()

@mock.patch('patch_tutorial2.temperature_sensor.convert_to')
def test_perform_conversion_C_to_F(mocked_function):
    mocked_function.return_value = 32
    result = PT2.perform_conversion(0, 'Fahrenheit')
    assert result == 'A reading of 0 degrees Celsius is equivalent to 32 degrees Fahrenheit'
    mocked_function.assert_called_with(0, 'Fahrenheit')