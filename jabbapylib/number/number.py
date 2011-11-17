#!/usr/bin/env python

"""
Working with numbers.

# from jabbapylib.number.number import number_to_pretty_string
"""

def number_to_pretty_string(n):
    """Converts a number to a nicely formatted string.
    
    Example: 6874 => '6,874'."""
    l = []
    for i, c in enumerate(str(n)[::-1]):
        if i % 3 == 0 and i != 0:
            l += ','
        l += c
    return "".join(l[::-1])

#############################################################################
    
if __name__ == "__main__":
    number = 6874
    print number_to_pretty_string(number)   # '6,874' 