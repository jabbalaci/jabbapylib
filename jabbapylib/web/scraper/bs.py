#!/usr/bin/env python

"""
Working with BeautifulSoup.
"""

from jabbapylib.web import web

from BeautifulSoup import BeautifulSoup


def to_soup(html_source):
    """Convert HTML source (text) to soup object."""
    return BeautifulSoup(html_source)

def prettify(soup):
    """Prettify HTML source. The HTML source is in a soup object."""
    return soup.prettify()

#############################################################################

if __name__ == "__main__":
    url = "http://index.hu"
    text = web.get_page(url)
    soup = to_soup(text)
    print prettify(soup)