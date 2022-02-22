import pytest
import user_info
from mock import Mock, patch

def test_get_user_info_older():
    user_responses = 'Luis'
    expected_output = "Luis was born on 4 BBY"
    with patch('builtins.input', side_effect=user_responses):
        assert user_info.get_user_info() == expected_output

def test_get_user_year_younger():
    user_info.input = Mock(return_value = "1979")
    expected_output = "You were born on 2 ABY"
    assert user_info.get_user_year() == expected_output