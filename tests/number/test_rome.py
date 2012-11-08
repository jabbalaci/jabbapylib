from jabbapylib.number import rome as roman


def test_roman_to_decimal():
    assert roman.roman_to_decimal('MCMLXXVII') == 1977
    assert roman.roman_to_decimal('MCCCCCCVI') == 1606
    assert roman.roman_to_decimal('') == 0
    assert roman.roman_to_decimal('ix') == 9

def test_decimal_to_roman():
    assert roman.decimal_to_roman(49) == 'XLIX'
    assert roman.decimal_to_roman(9) == 'IX'
    assert roman.decimal_to_roman(0) == 'Nulla'
    assert roman.decimal_to_roman(125) == 'CXXV'

def test_simplify_roman():
    assert roman.simplify_roman('MCCCCCCVI') == 'MDCVI'
    assert roman.simplify_roman('IIII') == 'IV'