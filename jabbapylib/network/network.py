#!/usr/bin/env python

"""
Network-related stuff.

# from jabbapylib.network import network
"""

import urllib2 #@UnusedImport
import jabbapylib.web.web as web
from jabbapylib.web.web import get_page

URL = 'http://www.google.com'


def is_internet_on(method=1):
    """Check if the Internet connection is on."""
    
    if method == 1:
        # At my current place we have a wifi that redirects to a login page,
        # so we always have a connection. That's why I check the content of
        # the fetched webpage.
        text = web.get_page(URL)
        if text:
            if '<title>Google</title>' in text:
                return True
        # else:
        return False
    elif method == 2:
        # http://stackoverflow.com/questions/3764291/checking-network-connection
        try:
            urllib2.urlopen('http://www.google.com', timeout=1)
            return True
        except urllib2.URLError: 
            return False
    else:
        print '# warning: unknown method in is_internet_on()'
        
        
def get_my_external_ip():
    """
    Get my external IP.
    
    Local IP: http://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
    """
    return get_page('http://ifconfig.me/ip')
   
#############################################################################
    
if __name__ == "__main__":
    print is_internet_on()
    print get_my_external_ip()
    