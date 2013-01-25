#!/usr/bin/env python

"""
Find a window by its name, get its window ID, bring it to foreground, etc.

required package: xdotool (sudo apt-get install xdotool)

# from jabbapylib.window import window
"""

import os
import re
from jabbapylib.process.process import get_simple_cmd_output
from cStringIO import StringIO


def get_window_title_by_id(wid):
    result = get_simple_cmd_output('xwininfo -id {id}'.format(id=wid))
    for line in StringIO(result):
        line = line.rstrip("\n")
        match = re.search(r'^xwininfo: Window id:.*"(.*)"$', line)
        if match:
            return match.group(1)
    #
    return None


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
    print get_window_title_by_id(wid)