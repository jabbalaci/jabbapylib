#!/usr/bin/env python

"""
# from jabbapylib.platform import platform
"""

import os
import sys
import getpass
import socket


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

#############################################################################

if __name__ == "__main__":
    print get_hostname()
    print get_home_dir()
    print get_username()
    print is_linux()
