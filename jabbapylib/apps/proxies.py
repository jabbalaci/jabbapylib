#!/usr/bin/env python

"""
Proxy Explorer

Extract list from http://www.ip-adress.com/proxy_list/, then
test proxies to see if they work.
"""

import urllib
from jabbapylib.web.scraper import bs
from jabbapylib.web.web import get_page
import socket

BASE = 'http://www.ip-adress.com/proxy_list/'
TIMEOUT = 5    # in seconds


class Proxy(object):
    """
    Class for proxy objects.
    """
    def __init__(self, ip, type, country):
        self.ip = ip
        self.type = type
        self.country = country
               
    def __str__(self):
        d = dict()
        d['ip'] = self.ip
        d['type'] = self.type
        d['country'] = self.country
        return str(d)
        
        
def check(proxy):
    """
    Test proxy. 
    
    Return True if it's working; return False otherwise. 
    """
    socket.setdefaulttimeout(TIMEOUT)
    proxies = {'http': 'http://'+proxy.ip}
    result = False
    try:
        urllib.urlopen("http://www.google.com", proxies=proxies)
        result = True
    except IOError:
        result = False
    socket.setdefaulttimeout(None)
    #
    return result


def extract_list():
    """
    Extract proxy list from base url.
    """
    proxies = []    
    text = get_page(BASE, user_agent=True)
    soup = bs.to_soup(text)
    proxylist = soup.findCssSelect('table.proxylist')[0] 
    for tr in proxylist.findAll('tr', {'class': True}):
        if tr['class'] in ('odd', 'even'):
            cols = tr.findAll('td')
            ip = cols[0].text
            type = cols[1].text
            country = cols[2].text
            proxies.append(Proxy(ip, type, country))
    #
    return proxies

     
def filter(proxies, type=None, country='United States'):
    """
    Filter proxies by type and country.
    
    Maybe best proxies have type 'Elite'.
    """
    if type:
        proxies = [p for p in proxies if p.type == type]
    if country:
        proxies = [p for p in proxies if p.country == country]
    #
    return proxies


def get_working_proxies(proxies):
    """
    Filter working proxies.
    """
    working = []
    for p in proxies:
        if check(p):
            working.append(p)
    #
    return working


def main():
    proxies = extract_list()
    proxies = filter(proxies)    
    working = get_working_proxies(proxies)
    
    print 'Working US proxies:'
    for p in working:
        print '({n}) {p}'.format(n=len(working), p=p)
    if len(working) == 0:
        print 'None'
    else:
        print '__END__'

#############################################################################

if __name__ == "__main__":
    main()
