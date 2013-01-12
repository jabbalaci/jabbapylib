#!/usr/bin/env python

import requests
#import requests1 as requests
import socket
import termcolor
import httplib
from jabbapylib.process.timeout import Timeout
from jabbapylib.process import process
import urllib2

TIMEOUT = 10
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:17.0) Gecko/17.0 Firefox/17.0'
headers = {}
headers['user-agent'] = USER_AGENT
GOOGLE_URL = "http://www.google.com"


def fetch_with_urllib2(url, proxy):
    socket.setdefaulttimeout(TIMEOUT)
    opener = urllib2.build_opener(urllib2.ProxyHandler({'http': proxy}))
    opener.addheaders = [('User-agent', USER_AGENT)]
    urllib2.install_opener(opener)
    try:
        r = None
        with Timeout(TIMEOUT):
            r = urllib2.urlopen(url)
        if r:
            return r.read()
    except (requests.exceptions.Timeout,
            requests.exceptions.ConnectionError,
            httplib.IncompleteRead):
        return False
    except urllib2.HTTPError:
        return False
    except httplib.BadStatusLine:
        return False
    except urllib2.URLError:
        return False
    except socket.timeout:
        return False
    except socket.error:
        return False
    except Timeout.Timeout:
        return False
    except RuntimeError:
        return False

    # if we get here:
    return False


def fetch_with_requests(url, proxy):
    socket.setdefaulttimeout(TIMEOUT)
    proxies = {'http': 'http://'+proxy}
    try:
        r = None
        with Timeout(TIMEOUT):
            r = requests.get(GOOGLE_URL, proxies=proxies, headers=headers, timeout=TIMEOUT)
        if r:
            return r.text
    except (requests.exceptions.Timeout,
            requests.exceptions.ConnectionError,
            httplib.IncompleteRead):
        return False
    except socket.timeout:
        print termcolor.colored('# socket timeout'.format(proxy), 'red')
        return False
    except socket.error:
        print termcolor.colored('# socket error'.format(proxy), 'red')
        return False
    except Timeout.Timeout:
        print termcolor.colored('# timeout'.format(proxy), 'red')
        return False
    except RuntimeError:
        print termcolor.colored('# runtime error'.format(proxy), 'red')
        return False

    # if we get here:
    return False

#############################################################################

if __name__ == "__main__":
    proxy = '87.250.37.50:800'
#    print fetch_with_urllib2(GOOGLE_URL, proxy)
    print fetch_with_requests(GOOGLE_URL, proxy)