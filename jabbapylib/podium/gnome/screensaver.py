#!/usr/bin/env python

"""
Activate/deactivate the Gnome screensaver.

# from jabbapylib.podium.gnome.screensaver import screensaver
"""

import os
from time import sleep


def screensaver(set):
    """
    Activate/deactivate the screensaver.

    Here I suppose you use gnome-screensaver.
    The parameter "set" can be True or False.
    """
    set = '-a' if set else '-d'
    cmd = 'gnome-screensaver-command {set}'.format(set=set)
    os.system(cmd)

def lock_screen():
    """
    Lock the screen (demands your password).
    """
    os.system('gnome-screensaver-command -l')

def unlock_screen():
    """
    Unlock the screen (without entering your password).
    """
    os.system('gnome-screensaver-command -d')

#############################################################################

if __name__ == "__main__":
    print 'Blanking and un-blanking the screen...'
    sleep(2)
    screensaver(True)
    sleep(2)
    screensaver(False)
    #
    print 'Locking and unlocking the screen...'
    sleep(2)
    lock_screen()
    sleep(5)
    unlock_screen()