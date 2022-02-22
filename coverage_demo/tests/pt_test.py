'''
Sample code to demonstrate unit testing
'''
import pytest
import target

def test_welcome_person_student():
    expected_return = 'Welcome Anakin, hope you enjoy the class'
    assert target.welcome_person('Anakin', 'student') == expected_return

def test_welcome_person_instructor():
    expected_return = 'Welcome Obi-Wan, break a leg!'
    assert target.welcome_person('Obi-Wan', 'instructor') == expected_return

def test_welcome_person_unknown_role():
    expected_return = 'Error, the role entered by Yoda does not exist'
    assert target.welcome_person('Yoda', 'Jedi Master') == expected_return