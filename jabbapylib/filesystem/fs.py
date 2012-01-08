#!/usr/bin/env python

"""
file system operations

# from jabbapylib.filesystem import fs
"""

import urlparse
from jabbapylib.dateandtime.dateandtime import get_timestamp_from_year_to_second


def read_first_line(input_file):
    """Read the first line of a file.
    
    Useful to read username, password, etc.
    Security tip: store such files on a Truecrypt volume."""
    f = open(input_file, 'r')
    line = f.readline().rstrip('\n')
    f.close()
    
    return line


def is_local_path(path):
    """Decide if path is a local file. It can
    be a URL too. The path can point to
    a non-existing file too."""
    p = urlparse.urlparse(path)
    return (not p.scheme and not p.netloc)


def get_timestamped_filename():
    """Return a timestamped text filename."""
    return '{ts}.txt'.format(ts=get_timestamp_from_year_to_second())

############################################################################# 
 
if __name__ == "__main__":
    input_file = '/home/jabba/secret/project_euler/username.txt'
    print read_first_line(input_file)
    #
    path = 'http://google.com'
    print is_local_path(path)
    print get_timestamped_filename()