from jabbapylib.number import number


def test_number_to_pretty_string():
    assert number.number_to_pretty_string(1977) == '1,977'
    assert number.number_to_pretty_string(1234567) == '1,234,567'
    assert number.number_to_pretty_string(123) == '123'
    
def test_sizeof_fmt():
    assert number.sizeof_fmt(23) == '23.0 bytes'
    assert number.sizeof_fmt(1234) == '1.2 KB'
    assert number.sizeof_fmt(1234567) == '1.2 MB'
    assert number.sizeof_fmt(1234567890) == '1.1 GB'
    assert number.sizeof_fmt(1234567890123) == '1.1 TB'
    assert number.sizeof_fmt(123456789012357) == '112.3 TB'