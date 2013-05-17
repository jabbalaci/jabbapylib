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
from jabbapylib.filesystem import fs


def get_window_title_by_id(wid):
    assert fs.which("xwininfo"), "the program xwininfo was not found."
    #
    result = get_simple_cmd_output('xwininfo -id {id}'.format(id=wid))
    for line in StringIO(result):
        line = line.rstrip("\n")
        match = re.search(r'^xwininfo: Window id:.*"(.*)"$', line)
        if match:
            return match.group(1)
    #
    return None


def get_active_window_id(hexa=False):
    """
    Window ID of the active window.

    The return value is a string. By default, the ID is in decimal
    format. If hexa is True, the return value is hexadecimal.
    In both cases, the return value is a string.
    """
    assert fs.which("xdotool"), "the program xdotool was not found."
    #
    wid = get_simple_cmd_output('xdotool getactivewindow').strip()
    if not hexa:
        return wid
    else:
        return hex(int(wid))


def activate_window_by_id(wid):
    """
    Put the focus on and activate the the window with the given ID.
    """
    assert fs.which("xdotool"), "the program xdotool was not found."
    #
    os.system('xdotool windowactivate {wid}'.format(wid=wid))


def toggle_fullscreen(wid_hexa):
    """
    Toggle the given window to fullscreen.

    The window id is a hexa string.
    """
    assert fs.which("wmctrl"), "the program wmctrl was not found."
    #
    cmd = "wmctrl -i -r {wid} -b toggle,maximized_vert,maximized_horz".format(wid=wid_hexa)
    os.system(cmd)

#############################################################################

if __name__ == "__main__":
    wid = get_active_window_id()
    print wid
    wid_hexa = get_active_window_id(hexa=True)
    print wid_hexa
    activate_window_by_id(wid)
    print get_window_title_by_id(wid)
    toggle_fullscreen(wid_hexa)