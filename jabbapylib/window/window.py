#!/usr/bin/env python

"""
Find a window by its name, get its window ID, bring it to foreground, etc.

required package: xdotool (sudo apt-get install xdotool)

# from jabbapylib.window import window
"""

import os
from jabbapylib.process.process import get_simple_cmd_output


def get_active_window_id():
    """
    Window ID of the active window.

    The return value is a string.
    """
    return get_simple_cmd_output('xdotool getactivewindow').strip()


def activate_window_by_id(wid):
    """
    Put the focus on and activate the the window with the given ID.
    """
    os.system('xdotool windowactivate {wid}'.format(wid=wid))

#############################################################################

if __name__ == "__main__":
    wid = get_active_window_id()
    print wid
    activate_window_by_id(wid)