#!/usr/bin/env python

"""
Find a window by its name, get its window ID, bring it to foreground, etc.

required package: xdotool (sudo apt-get install xdotool)

# from jabbapylib.window import window
"""

import os
import re
from collections import OrderedDict
from cStringIO import StringIO

from jabbapylib.filesystem import fs
from jabbapylib.process import process
from jabbapylib.process.process import get_simple_cmd_output


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


def get_wmctrl_output():
    """
    Parses the output of wmctrl and returns a list of ordered dicts.
    """
    assert fs.which("wmctrl"), "the program wmctrl was not found."
    #
    cmd = "wmctrl -lGpx"
    lines = [line for line in process.get_simple_cmd_output(cmd).split("\n") if line]

    res = []
    for line in lines:
# 0x05e000c7  0 4402   2562 298  638  540  truecrypt.Truecrypt   jabba-uplink TrueCrypt
        pieces = line.split()
        d = OrderedDict()
        #d['wid'] = int(pieces[0], 16)  # converted to decimal
        d['wid'] = pieces[0]
        d['desktop'] = int(pieces[1])
        d['pid'] = int(pieces[2])
        d['geometry'] = [int(x) for x in pieces[3:7]]
        d['window_class'] = pieces[7]
        d['client_machine_name'] = pieces[8]
        d['window_title'] = ' '.join(pieces[9:])
        res.append(d)
    #
    return res


def get_wid_by_pid(pid):
    """
    Having a pid, return its wid.

    We have the PID of a process. Figure out its window ID.
    """
    for d in get_wmctrl_output():
        if d['pid'] == pid:
            return d['wid']
    #
    return None

#############################################################################

if __name__ == "__main__":
    wid = get_active_window_id()
    print wid
    wid_hexa = get_active_window_id(hexa=True)
    print wid_hexa
    activate_window_by_id(wid)
    print get_window_title_by_id(wid)
#    toggle_fullscreen(wid_hexa)
    print get_wmctrl_output()
    print get_wid_by_pid(9491)
