from unittest.mock import Mock, patch
import ssn_collector

def test_validate_number_true():
    test_number = "12345678"
    assert ssn_collector.validate_number(test_number) is True

def test_validate_number_false():
    test_number = "0"
    assert ssn_collector.validate_number(test_number) is False

def test_user_input_with_mock():
    ssn_collector.input = Mock(return_value="12344")
    test_number = "12344"
    assert ssn_collector.get_number() == test_number

def test_user_input_with_patch():
    test_number = "12344"
    with patch('ssn_collector.input', side_effect=("12344", "2347329874092374902398")):
        assert ssn_collector.get_number() == test_number
        assert ssn_collector.get_number() == "Invalid SSN"

def test_personal_data_with_patch():
    sequence_of_responses = (
        "Paul", 
        "Lockaby"
        )
    with patch('ssn_collector.input', side_effect=sequence_of_responses):
        assert ssn_collector.get_personal_data() == ("Paul", "Lockaby")