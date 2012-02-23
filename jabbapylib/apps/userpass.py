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

def get_password(min=8, max=8):
    """
    Create a password with uppercase letters, lowercase letters, and digits.
    
    The password will include lowercase letters with higher probability.
    """
    assert min <= max
    #
    chars = string.ascii_lowercase + string.ascii_lowercase + string.ascii_lowercase + \
            string.ascii_uppercase + string.digits + string.digits + string.digits
    chars = ''.join(my_shuffle([x for x in chars]))
    return ''.join(choice(chars) for x in range(randint(min, max)))

#############################################################################

if __name__ == "__main__":
    print get_username()
    print get_password()
