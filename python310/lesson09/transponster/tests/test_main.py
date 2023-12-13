'''
This module will handle testing for main.py
'''
from transponster import main

def test_simplify_name_four_names():
    test_name = "Luis Diego Conejo Alpizar"
    assert main.simplify_name(test_name) == "Luis Conejo"

def test_simplify_name_three_names():
    test_name = "Luis Diego Conejo"
    assert main.simplify_name(test_name) == "Luis Conejo"

def test_simplify_name_two_names():
    test_name = "Luis Conejo"
    assert main.simplify_name(test_name) == "Luis Conejo"

def test_simplify_name_invalid_name():
    test_name = "Joe"
    assert main.simplify_name(test_name) == "Invalid Name"

def test_simplify_name_invalid_type():
    test_name = 99
    assert main.simplify_name(test_name) == "Invalid Name"

def test_deconstruct_name():
    test_name = "Luis Diego Conejo Alpizar"
    result = main.deconstruct_name(test_name)
    test_values = {
        'name': 'Luis',
        'middle_name': 'Diego',
        'last_name_1': 'Conejo',
        'last_name_2': 'Alpizar'
    }

    for key, value in test_values.items():
        assert result[key] == value 
    