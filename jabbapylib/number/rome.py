#!/usr/bin/env python

"""
Convert Roman numbers to decimal.
Convert decimal to Roman numbers.

It's just a wrapper for the module 
romanclass (http://pypi.python.org/pypi/romanclass).

from jabbapylib.number import rome as roman
"""

from jabbapylib.lib import romanclass as roman


def roman_to_decimal(num):
    """
    Convert a Roman number to decimal.
    """
    return roman.fromRoman(num)

def decimal_to_roman(num):
    """
    Convert a decimal number to Roman.
    """
    return roman.toRoman(num)

def simplify_roman(num):
    """
    Given a Roman number, simplify it.
    """
    return decimal_to_roman(roman_to_decimal(num))

#############################################################################
    
if __name__ == "__main__":
    print roman_to_decimal('MCMLXXVII')
    print roman_to_decimal('MMMMMMDCLXXII')
    #
    print decimal_to_roman(49)
    print simplify_roman('IIII')
