from jabbapylib.number import number


def test_number_to_pretty_string():
    assert number.number_to_pretty_string(1977) == '1,977'
    assert number.number_to_pretty_string(1234567) == '1,234,567'
    assert number.number_to_pretty_string(123) == '123'