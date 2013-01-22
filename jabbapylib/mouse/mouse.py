#!/usr/bin/env python

"""
Mouse actions.

What we need is:
* move the mouse pointer to a given position
* perform a simple left click

# from jabbapylib.mouse import mouse
"""

import time
import autopy as ap
from autopy.mouse import LEFT_BUTTON


#def left_down():
#    ap.mouse.toggle(True, LEFT_BUTTON)
#    time.sleep(.1)
#    print '# left down'
#
#
#def left_up():
#    ap.mouse.toggle(False, LEFT_BUTTON)
#    time.sleep(.1)
#    print '# left release'


def left_click():
    """Perform a left mouse click."""
    ap.mouse.click(LEFT_BUTTON)
    time.sleep(.1)
#    print "# click"


def move_xy(x, y):
    """Move the mouse pointer to the given position."""
    ap.mouse.move(x, y)


def move_to(pos):
    """
    Move the mouse pointer to the given position.

    pos is a tuple
    """
    move_xy(pos[0], pos[1])


def click_to(pos):
    """
    Perform a left mouse click at the given position.

    pos is a tuple
    """
    move_to(pos)
    left_click()


def get_pos():
    return ap.mouse.get_pos()

#############################################################################

if __name__ == "__main__":
    time.sleep(3)
    print '# absolute pos:', get_pos()
