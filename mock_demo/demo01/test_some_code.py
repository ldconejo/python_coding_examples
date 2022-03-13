from mock import Mock, patch
import some_code

def test_get_user_info():
    some_code.input = Mock(return_value = 'Luis')
    assert some_code.get_user_info() == 'Luis'

def test_get_more_user_info():
    responses = ('Luis', 'Conejo', '41')
    expected_return = "Luis Conejo is 41 years old"
    with patch('some_code.input', side_effect=responses):
        assert some_code.get_more_user_info() == expected_return