'''
Sample code to demonstrate unit testing
'''
from unittest.mock import patch
import pytest
import target

def test_main_menu_addition():
    '''
    Tests main_menu() using addition
    '''
    user_responses = ('Luis', 'addition', '12', '11')
    expected_output = "The result of adding 12 plus 11 is 23.0"
    with patch('builtins.input', side_effect=user_responses):
        assert target.main_menu() == expected_output

def test_main_menu_subtraction():
    '''
    Tests main_menu() using subtraction
    '''
    # Since we are 'patching' (overriding) the input function,
    # we need to define what the 'user' answers will be
    user_responses = ('Luis', 'subtraction', '23', '10')
    # Also need to define the expected output
    expected_output = "The result of subtracting 23 minus 10 is 13.0"
    # Patch will override Python's input function, sending one value
    # from user_responses every time main_menu() calls input
    with patch('builtins.input', side_effect=user_responses):
        assert target.main_menu() == expected_output

def test_addition_normal():
    '''
    Tests addition in a normal case
    '''
    expected_output = 42.0
    assert target.perform_addition('22', '20') == expected_output

def test_subtraction_normal():
    '''
    Tests subtraction in a normal case
    '''
    expected_output = 2.0
    assert target.perform_subtraction('22', '20') == expected_output

def test_addition_value_error():
    '''
    Tests addition with invalid parameters triggering a ValueError exception
    '''
    # This is how you test for exceptions in Pytest
    # the use of a context manager (the 'with' keyword) is examined later
    # in the course
    with pytest.raises(ValueError):
        target.perform_addition('non', 'sense')
