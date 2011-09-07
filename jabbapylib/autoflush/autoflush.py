#!/usr/bin/env python

"""
Switch autoflush on.
"""

import sys
import os


def unbuffered():
    """Switch autoflush on."""
    # reopen stdout file descriptor with write mode
    # and 0 as the buffer size (unbuffered)
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    
#############################################################################
    
if __name__ == "__main__":
    unbuffered()
    print "unbuffered text"