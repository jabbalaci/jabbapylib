#!/usr/bin/env python

"""
Proxy Explorer

Extract list from http://www.ip-adress.com/proxy_list/, then
test proxies to see if they work.
"""

import sys
import urllib
import operator
from jabbapylib.web.scraper import bs
from jabbapylib.web.web import get_page
from jabbapylib.network import ping
from jabbapylib.autoflush.autoflush import unbuffered
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
        self.avg_time = self.get_avg_time(self.ip)
        
    def get_avg_time(self, ip):
        """Average response time of the server."""
        ip = ip.split(':')[0]
        return ping.ping(ip)
               
    def __str__(self):
        d = dict()
        d['ip'] = self.ip
        d['type'] = self.type
        d['country'] = self.country
        d['avg_time'] = self.avg_time
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
    sys.stdout.write('# extracting list')
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
            sys.stdout.write('.')
    #
    print 'done.'
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
#        if check(p):
        if p.avg_time is not None:
            working.append(p)
    #
    return working


def main():
    proxies = extract_list()
    proxies = filter(proxies)    
    working = get_working_proxies(proxies)
    working.sort(key=operator.attrgetter("avg_time"), reverse=False)
    
    print 'Working US proxies:'
    for i,p in enumerate(working):
        print '({n}) {p}'.format(n=i+1, p=p)
    if len(working) == 0:
        print 'None'
    else:
        print '__END__'

#############################################################################

if __name__ == "__main__":
    unbuffered()
    main()
