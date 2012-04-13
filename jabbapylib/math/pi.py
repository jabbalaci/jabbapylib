#!/usr/bin/env python

"""
Get the first X digits of PI (after the dot).

I will only store the digits after the dot, i.e. "3." is dropped.

# from jabbapylib.math import pi
"""

import os
import re
import sys
from cStringIO import StringIO
from jabbapylib.hash.hash import file_to_md5
from jabbapylib.web import web


"""
first part
==========

Instead of calculating the digits, I simply download the result :)

Number of digits can be:
* 1000 decimal places (pi3)
* 10000 decimal places (pi4)
* 100000 decimal places (pi5)
* 1000000 decimal places (pi6)

Data are downloaded from http://newton.ex.ac.uk/research/qsystems/collabs/pi/ .

The specified file is downloaded to /tmp for caching purposes.
"""

URL = 'http://newton.ex.ac.uk/research/qsystems/collabs/pi'
PI3 = 'pi3.txt'
PI3_MD5HASH = '410d8c808f7e5524fe208b74511f05c6' 
PI4 = 'pi4.txt'
PI4_MD5HASH = 'b90eaade5badaf8753efe41022f1e848'
PI5 = 'pi5.txt'
PI5_MD5HASH = '07638c90a57e93693d38d938a0dd9293'
PI6 = 'pi6.txt'
PI6_MD5HASH = '0e2c68f96dab3293917ec0eb6165898d'
TMP_DIR = '/tmp'

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
    fname = '{tmp}/{data}'.format(tmp=TMP_DIR, data=data)
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

"""
second part
===========

This part is based on http://mail.python.org/pipermail/edu-sig/2006-July/006810.html .

Quote:

    Here's a generator I coded up based on a paper by Gibbons:
       http://web.comlab.ox.ac.uk/oucl/work/jeremy.gibbons/publications/spigot.pdf
    
    It's simple to code, but I think you have to read the paper to figure out what 
    it's doing. (I just translated some code, so I really can't tell you :-) In 
    the paper, this was done in a lazy functional language. I was mostly 
    interested to see how it would translate to a Python generator.
    
    # pi.py -- imlementation of Gibbons' spigot algorithm for pi
    # John Zelle 4-5-06
    
    Here it is in action:
    
    >>> import pi
    >>> digits = pi.pidigits()
    >>> for i in range(30): print digits.next(),
    ...
    3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2 6 4 3 3 8 3 2 7
    >>>     
    
    Since this uses long ints, it slows down considerably after a few thousand 
    digits. You might want to use psyco when generating really "deep" digits.
    
    --John
"""

def pi_digits():
    """generator for digits of pi"""
    q,r,t,k,n,l = 1,0,1,1,3,3
    while True:
        if 4*q+r-t < n*t:
            yield n
            q,r,t,k,n,l = (10*q,10*(r-n*t),t,k,(10*(3*q+r))/t-10*n,l)
        else:
            q,r,t,k,n,l = (q*k,(2*q+r)*l,t*l,k+1,(q*(7*k+2)+r*l)/(t*l),l+2)
            
def get_digits(size):
    buf = StringIO()
    digits = pi_digits()
    digits.next()    # skip "3", start from the first digit after the dot

    for _ in xrange(size):
        buf.write((str(digits.next())))
        
    return buf.getvalue()

#############################################################################

"""
third part
==========

Quote from E. Woiski:

    Easy. Use mpmath (alone or under sympy):
    
    >>> from sympy.mpmath import mp
    >>> mp.dps = 200000
    >>> +mp.pi
    
    ... and there you are: 200000 digits of pi :)
    
Requires you to install python-sympy (via apt-get).
"""

def get_pi(size):
    """size is the number of digits after the dot"""
    from sympy.mpmath import mp
    mp.dps = size + 1
    return str(mp.pi)[2:]   # cut "3." off

#############################################################################

if __name__ == "__main__":
# first version
#    main(PI3)   # PI3 means: till 10^3 = 1000. Max: PI6.
    
# second version
#    print get_digits(1000)

# third version
    print get_pi(10000)