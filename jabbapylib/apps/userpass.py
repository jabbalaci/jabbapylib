#!/usr/bin/env python

"""
Username and password generator.

Made for online registrations.

# from jabbapylib.apps import userpass
"""

import string
from random import shuffle, choice, randint
from jabbapylib.lib import markov_passwords

#############################################################################

#import os
#import urllib
#from urlparse import urlparse
#from jabbapylib.web import web

#BASE1 = 'http://myusernamegenerator.com?'
#
#def get_username():
#    url = BASE1 + urllib.urlencode({'category' : 'short'})
#    redirection = web.get_redirected_url(url).lower()
#    return os.path.split(urlparse(redirection)[2])[1]

def get_username(length=6):
    """
    Returns a readable (Japanese-style) username.
    """
    return markov_passwords.get_word(length)

#############################################################################

def my_shuffle(array):
    """
    Returns a shuffled array.

    random.shuffle shuffles in place and returns None. This way shuffle can be
    used in a chain.
    """
    shuffle(array)
    return array


def get_password(length=8):
    """
    Create a password with uppercase letters, lowercase letters, and digits.

    The password will include lowercase letters with higher probability.
    """
    assert length >= 8
    #
    chars = string.ascii_lowercase + string.ascii_lowercase + string.ascii_lowercase + \
            string.ascii_uppercase + string.digits + string.digits + string.digits
    chars = ''.join(my_shuffle([x for x in chars]))
    return ''.join(choice(chars) for x in range(length))


def get_urandom_password(length=8):
    """
    Get data from /dev/urandom .
    """
    assert length >= 8
    #
    li = []
    with open("/dev/urandom") as f:
        while len(li) < length:
            c = f.read(1)
            if c.isalnum():
                li.append(c)

    return ''.join(li)

#############################################################################

if __name__ == "__main__":
    print get_username()
    print get_password(length=12)
    print
    print get_urandom_password(length=12)
