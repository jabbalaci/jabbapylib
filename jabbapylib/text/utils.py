#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Text manipulations.

# from jabbapylib.text.utils import inc_string
"""


def inc_string(text):
    """
    Increase a string by one.

    Examples: a -> b, e -> f, z -> aa, af -> ag.
    """
    text = list(text[::-1])
    go_over = False
    for index, c in enumerate(text):
        if index == 0 or go_over:
            up = chr(ord(c)+1)
        if up <= 'z':
            go_over = False
            text[index] = up
            break
        else:
            go_over = True
            text[index] = 'a'

    if go_over:
        text.append('a')

    return ''.join(text[::-1])

#############################################################################
    
if __name__ == "__main__":
    print 'a ->', inc_string('a')
    print 'f ->', inc_string('f')
    print 'z ->', inc_string('z')
    print 'af ->', inc_string('af')
    print 'zz ->', inc_string('zz')
