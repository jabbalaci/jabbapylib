#!/usr/bin/env python

"""
Get the first X digits of PI. Instead of calculating them,
I simply dowmload the result :)

TODO: figure out how to do it in a more elegant way.

Number of digits can be:
* 1000 decimal places (pi3)
* 10000 decimal places (pi4)
* 100000 decimal places (pi5)
* 1000000 decimal places (pi6)

Data are downloaded from http://newton.ex.ac.uk/research/qsystems/collabs/pi/ .

I will only store the digits after the dot, i.e. "3." is dropped.

The specified file is downloaded to /tmp for caching purposes.

# from jabbapylib.math import pi
"""

import os
import re
import sys
from cStringIO import StringIO
from jabbapylib.hash.hash import file_to_md5
from jabbapylib.web import web

URL = 'http://newton.ex.ac.uk/research/qsystems/collabs/pi'
PI3 = 'pi3.txt'
PI3_MD5HASH = '410d8c808f7e5524fe208b74511f05c6' 
PI4 = 'pi4.txt'
PI4_MD5HASH = 'b90eaade5badaf8753efe41022f1e848'
PI5 = 'pi5.txt'
PI5_MD5HASH = '07638c90a57e93693d38d938a0dd9293'
PI6 = 'pi6.txt'
PI6_MD5HASH = '0e2c68f96dab3293917ec0eb6165898d'

def validate(fname):
    try:
        result = re.search('/pi([3-6])\.txt$', fname)
        assert result
        hash = 'PI{n}_MD5HASH'.format(n=result.group(1))
        assert file_to_md5(fname) == globals()[hash]
        return True
    except AssertionError:
        return False

def download(data, fname):
    url = URL + '/' + data
    web.download_to(url, fname) 

def check(fname):
    if not validate(fname):
        print >>sys.stderr, "Error: {f} is corrupted.".format(f=fname)
        sys.exit(1)

def read_digits(fname):
    buf = StringIO()
    with open(fname) as f:
        for line in f:
            line = line.rstrip('\n').replace(' ', '')
            if len(line) == 50:
                buf.write(line)
                
    return buf.getvalue()

def get_digits_of(data):
    fname = '/tmp/{data}'.format(data=data)
    if os.path.isfile(fname):
        check(fname)
    else:
        download(data, fname)
        check(fname)
    # now read it
    return read_digits(fname)
    
def main(data):
    digits = get_digits_of(data)
    print digits

#############################################################################

if __name__ == "__main__":
    main(PI3)