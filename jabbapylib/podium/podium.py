#!/usr/bin/env python

"""
"podium" is in the standard library, so it was renamed to podium :)

# from jabbapylib.podium import podium
"""

import os
import sys
import getpass
import socket
from jabbapylib.process import process
from jabbapylib.filesystem import ini
from jabbapylib import config as cfg
import platform as p
from jabbapylib.hash.hash import string_to_md5


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

def get_firefox_profile_folder():
    """
    Location of Firefox's default profile folder. Typically, it looks like this:
    $HOME/.mozilla/firefox/xxxxxxxx.default .
    """
    ini_file = '{home}/.mozilla/firefox/profiles.ini'.format(home=get_home_dir())
    folder = ini.read_ini('Profile0', ini_file)['path']
    return '{home}/.mozilla/firefox/{folder}'.format(home=get_home_dir(), folder=folder)

def get_fingerprint(md5=False):
    """
    Fingerprint of the current operating system/platform.

    If md5 is True, a digital fingerprint is returned.
    """
    sb = []
    sb.append(p.node())
    sb.append(p.architecture()[0])
    sb.append(p.architecture()[1])
    sb.append(p.machine())
    sb.append(p.processor())
    sb.append(p.system())
    text = '#'.join(sb)
    if md5:
        return string_to_md5(text)
    else:
        return text

def get_short_fingerprint(length=6):
    """
    A short digital fingerprint of the current operating system/platform.

    Length should be at least 6 characters.
    """
    assert 6 <= length <= 32
    #
    return get_fingerprint(md5=True)[-length:]

#############################################################################

if __name__ == "__main__":
    print get_hostname()
    print get_home_dir()
    print get_username()
    print is_linux()
    print get_screen_resolution()
    print get_firefox_profile_folder()
    print get_fingerprint(True)
    print get_short_fingerprint()