#!/usr/bin/env python

"""
Working with webpages.
* download a page
* store a page (or image, etc.) in the file system
"""

import os
import sys
import urllib
import urllib2
import urlparse

from export_firefox_cookies import get_cookies_in_text, get_cookies_in_cookiejar
from jabbapylib.process import process


COOKIES_TXT = 'cookies.txt'


class MyOpener(urllib.FancyURLopener):
    """Custom user-agent."""
    version = 'Mozilla/5.0 (X11; Linux i686; rv:6.0.2) Gecko/20100101 Firefox/6.0.2'
# MyOpener


def get_referer(url):
    """Get the referer of a URL.
    
    Ex.: http://example.com/dir/file.html => http://example.com,
    i.e. keep the protocol and the host.
    """
    p = urlparse.urlparse(url)
    return "{0}://{1}".format(p.scheme, p.netloc)
# get_referer


def get_host(url):
    """Get the host from a URL.
    
    Example: http://projecteuler.net/index.php?section=statistics => projecteuler.net"""
    p = urlparse.urlparse(url)
    return p.netloc


def get_url_open(url, user_agent=False, referer=False):
    """Open a URL.
    
    This is a helper function for others who want to read the URL.
    """
    req = urllib2.Request(url)
    if user_agent:
        req.add_header('User-Agent', MyOpener.version)
    if referer:
        req.add_header('Referer', get_referer(url))
    try:
        return urllib2.urlopen(req)
    except urllib2.HTTPError:
        return None
# get_url_open


def get_url_info(url, user_agent=False, referer=False):
    """Get the meta-information of a page."""
    d = get_url_open(url, user_agent, referer)
    if d:
        result = d.info()
        d.close()
        return result
    # else
    return None
# get_url_info


def get_page(url, user_agent=False, referer=False):
    """Get the content of a page (HTML, image, etc.).
    
    Return value: string (can be binary too).
    """
    d = get_url_open(url, user_agent, referer)
    if d:
        result = d.read()
        d.close()
        return result
    # else
    return None
# get_page


def store_content_in_file(content, file_name, overwrite=False):
    """Store the content in a file."""
    if os.path.exists(file_name) and not overwrite:
        print >>sys.stderr, "# warning: {0} exists.".format(file_name)
        return False
    # else
    f = open(file_name, 'w')
    f.write(content)
    f.close()
    return True
# store_content_in_file


def get_page_with_cookies_using_wget(url):
    """Get the content of a cookies-protected page.
    
    The page is downloaded with wget. Cookies are passed to wget."""
    cookies = get_cookies_in_text(get_host(url))
    store_content_in_file(cookies, COOKIES_TXT, overwrite=True)
    OPTIONS = "--cookies=on --load-cookies={0} --keep-session-cookies".format(COOKIES_TXT)
    cmd = "/usr/bin/wget {options} '{url}' -qO-".format(options=OPTIONS, url=url)
    page = process.get_simple_cmd_output(cmd)
    os.unlink(COOKIES_TXT)
    
    return page


def get_page_with_cookies_using_cookiejar(url):
    """Get the content of a cookies-protected page.
    
    The page is downloaded with urllib2. The cookies are passed in a cookiejar."""
    cj = get_cookies_in_cookiejar(get_host(url))
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))      # cookies are added here
    urllib2.install_opener(opener)

    #txdata = None   # if we were making a POST type request, we could encode a dictionary of values here - using
    #params = {}
    #txdata = urllib.urlencode(params)
    #txheaders =  {'User-agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}          # fake a user agent, some websites (like google) don't like automated exploration
    #txheaders = {}
    #req = urllib2.Request(url, txdata, txheaders)            # create a request object

    req = urllib2.Request(url)
    handle = urllib2.urlopen(req)                               # and open it to return a handle on the url

    return handle.read()



#############################################################################

if __name__ == "__main__":
    #url = 'http://index.hu'
    #text = get_page(url)
    #print store_content_in_file(text, '/tmp/index.html', overwrite=True)
    url = 'http://projecteuler.net/index.php?section=statistics'
    #print get_page_with_cookies_using_wget(url)

    # version 2
    print get_page_with_cookies_using_cookiejar(url)