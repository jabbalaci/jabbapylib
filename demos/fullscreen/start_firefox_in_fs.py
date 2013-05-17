#!/usr/bin/env python

import os
from splinter import Browser
from jabbapylib.window import window
from jabbapylib.filesystem import fs


def toggle_fullscreen():
    assert fs.which("wmctrl"), "the program wmctrl was not found."
    #
    wid = window.get_active_window_id(hexa=True)
    cmd = "wmctrl -i -r {wid} -b toggle,maximized_vert,maximized_horz".format(wid=wid)
    os.system(cmd)

def main():
    browser = Browser()
    toggle_fullscreen()

#############################################################################

if __name__ == "__main__":
    main()