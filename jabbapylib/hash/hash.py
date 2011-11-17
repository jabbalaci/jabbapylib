#!/usr/bin/env python

"""
hashlib

# from jabbapylib.hash.hash import string_to_md5
# from jabbapylib.hash.hash import file_to_md5
"""

import hashlib


def string_to_md5(content):
    """Calculate the md5 hash of a string.
    
    This 'string' can be the binary content of a file too."""
    md5 = hashlib.md5()
    md5.update(content)
    return md5.hexdigest()


def file_to_md5(filename):
    """Calculate the md5 hash of a file. Memory-friendly solution,
    it reads the file piece by piece.
    
    http://stackoverflow.com/questions/1131220/get-md5-hash-of-a-files-without-open-it-in-python"""
    md5 = hashlib.md5()
    with open(filename,'rb') as f: 
        for chunk in iter(lambda: f.read(8192), ''): 
            md5.update(chunk)
    return md5.hexdigest()


#############################################################################
    
if __name__ == "__main__":
    text = 'uncrackable12'  # :)
    print string_to_md5(text)
    #
    filename = '/usr/bin/bash'
    print file_to_md5(filename)
