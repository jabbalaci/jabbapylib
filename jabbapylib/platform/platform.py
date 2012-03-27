#!/usr/bin/env python

"""
# from jabbapylib.platform import platform
"""

import os
import sys
import getpass
import socket
from jabbapylib.process import process
from jabbapylib import config as cfg


def get_hostname():
    """
    echo $HOSTNAME
    """
    return socket.gethostname()

def get_home_dir():
    """
    echo $HOME
    """
    return os.path.expanduser('~')

def get_username():
    """
    echo $USER
    """
    return getpass.getuser()

def is_linux():
    """
    Is the current platform Linux?
    """
    return sys.platform.startswith('linux')

def get_screen_resolution():
    """
    Screen resolution (as a tuple).
    """
    result = [x for x in process.get_simple_cmd_output(cfg.XRANDR).split('\n') if '*' in x][0]
    result = tuple([int(x) for x in result.split()[0].split('x')])
    return result

#############################################################################

if __name__ == "__main__":
    print get_hostname()
    print get_home_dir()
    print get_username()
    print is_linux()
    print get_screen_resolution()
