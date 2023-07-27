import target

def test_get_current_temperature():
    expected_result = "Current temperature is"
    assert expected_result in target.get_current_temperature()