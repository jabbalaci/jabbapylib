#!/usr/bin/env python

"""
Print colored text in the terminal.

# from jabbapylib.console import color
"""

from jabbapylib.lib.termcolor import colored

def color(text, color, attrs=[]):
    """Produce a colored text for the terminal."""
    return colored(text, color, attrs=attrs)

def bold(text, color='white'):
    return colored(text, color, attrs=['bold'])

##############################################################################

if __name__ == "__main__":
    print color('Everything is going perfectly fine.', 'green')
    print color('Reactor meltdown alert! Leave the building immediately!', 'red')
    print color('[ OK ]', 'cyan')
    print bold("Bold white color", 'white')
