#!/usr/bin/env python

"""
Process .ini configuration files.

# from jabbapylib.filesystem import ini
"""

import ConfigParser


def read_ini(section, fname):
    """Read the specified section of an .ini file."""
    conf = ConfigParser.ConfigParser()
    conf.read(fname)
    val = {}
    try:
        val = dict((v, k) for v, k in conf.items(section))
    except ConfigParser.NoSectionError:
        pass
    finally:
        return val

#############################################################################

if __name__ == "__main__":
    ini_file = '/home/jabba/.mozilla/firefox/profiles.ini'
    print read_ini('Profile0', ini_file)