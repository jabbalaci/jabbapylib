#!/usr/bin/env python

"""
Pronounce the word(s) given as parameters.
"""

import sys

from jabbapylib.say.say import say_with_google


def say(words):
    for w in words:
        say_with_google(w)

#############################################################################
    
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print 'Error: provide a word.'
        sys.exit(1)
    # else
    say(sys.argv[1:])