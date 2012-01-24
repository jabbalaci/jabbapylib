#!/usr/bin/env python

"""
Working with BeautifulSoup.

# from jabbapylib.web.scraper import bs
"""

import lx
import urlparse

from jabbapylib.web import web
from jabbapylib.lib.BeautifulSoup import BeautifulSoup
from lxml.html.builder import LI


def css_patch():
    """Add the function soup.findSelect (or soup.findCssSelect) to BeautifulSoup.
    
    From here: https://code.google.com/p/soupselect/."""
    from jabbapylib.lib import soupselect
    soupselect.monkeypatch()

def to_soup(html_source):
    """Convert HTML source (text) to soup object."""
    return BeautifulSoup(html_source)

def prettify(soup):
    """Prettify HTML source. The HTML source is in a soup object."""
    return soup.prettify()

def doc_to_soup(doc):
    return to_soup(lx.tostring(doc))

def get_links(soup, base_url=None):
    """
    Get the links on a webpage. If the URL of the given
    page is provided in base_url, then links are absolute.
    
    The soup object is NOT modified.
    """
    li = []
    for tag in soup.findAll('a', href=True):
        if base_url:
            link = urlparse.urljoin(base_url, tag['href'])
        else:
            link = tag['href']
             
        li.append(link)
        
    return li


def make_links_absolute(soup, base_url):
    """
    Replace relative links with absolute links.
    This one modifies the soup object.
    """
    assert base_url is not None
    #
    for tag in soup.findAll('a', href=True):
        tag['href'] = urlparse.urljoin(base_url, tag['href'])
    
    return soup


# The patch is applied automatically when this module is imported.
css_patch()

#############################################################################

if __name__ == "__main__":
    url = "http://index.hu"
    text = web.get_page(url)
    soup = to_soup(text)
    print prettify(soup)
    #
    
    LINKS = """
<html>
<head>
<title>retrogames.com</title>
</head>
<a href="http://retrogames.com">Retro Games HQ</a>
<a href="/games/elite">Elite</a>
<a href="/games/commando">Commando</a>
</html>
"""

    url = "http://retrogames.com"
    soup = to_soup(LINKS)
    for e in get_links(soup, base_url=url):
        print e