#!/usr/bin/env python

"""
Activate/deactivate the Gnome screensaver.

# from jabbapylib.podium.gnome.screensaver import screensaver
"""

import os
from time import sleep


def screensaver(set):
    """
    Activate/deactivate the scrrensaver.

    Here I suppose you use gnome-screensaver.
    The parameter "set" can be True or False.
    """
    set = '-a' if set else '-d'
    cmd = 'gnome-screensaver-command {set}'.format(set=set)
    os.system(cmd)

#############################################################################

if __name__ == "__main__":
    print 'Activating the screensaver in 2 seconds...'
    sleep(2)
    screensaver(True)
    sleep(2)
    screensaver(False)