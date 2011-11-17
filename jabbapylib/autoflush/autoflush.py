#!/usr/bin/env python

"""
Switch autoflush on.

# from jabbapylib.autoflush.autoflush import unbuffered
"""

import sys
import os

autoflush_on = False

def unbuffered():
    """Switch autoflush on."""
    global autoflush_on
    # reopen stdout file descriptor with write mode
    # and 0 as the buffer size (unbuffered)
    if not autoflush_on:
        sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
        autoflush_on = True
    
#############################################################################
    
if __name__ == "__main__":
    unbuffered()
    print "unbuffered text"