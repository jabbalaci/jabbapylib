#!/usr/bin/env python

"""
module mousepos (Linux only)

Get the current mouse coordinates.
"""

import os
import sys

# uses the package python-xlib
# from http://snipplr.com/view/19188/mouseposition-on-linux-via-xlib/
# or: sudo apt-get install python-xlib
from Xlib import display
 
def mousepos():
    """mousepos() --> (x, y) get the mouse coordinates on the screen (linux, Xlib)."""
    old_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    # this prints the string Xlib.protocol.request.QueryExtension to stdout,
    # that's why stdout is redirected temporarily to /dev/null
    data = display.Display().screen().root.query_pointer()._data
    sys.stdout = old_stdout
    
    return data["root_x"], data["root_y"]
 
############################################################################# 
 
if __name__ == "__main__":
    print("The mouse position on the screen is {0}".format(mousepos()))
