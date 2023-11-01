import target

def test_addition():
    math_tests = (
        (1,2,3),
        (4,5,9),
        (3,7,10)
    )
    for math_test in math_tests:
        expected_output = math_test[2]
        num1 = math_test[0]
        num2 = math_test[1]
        assert target.addition(num1, num2) == expected_output

def test_addition_default_values():
    expected_output = 6
    assert target.addition() == expected_output

def test_subtraction():
    expected_output = 3
    assert target.subtraction(7,4) == expected_output

def test_multiplication():
    expected_output = 15
    assert target.multiplication(5, 3) == expected_output

def test_division():
    expected_output = 30
    assert target.division(90, 3) == expected_output
