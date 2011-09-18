#!/usr/bin/env python

"""
Working with BeautifulSoup.
"""

import lx

from jabbapylib.web import web

from BeautifulSoup import BeautifulSoup


def css_patch():
    """Add the function soup.findSelect (or soup.findCssSelect) to BeautifulSoup.
    
    From here: https://code.google.com/p/soupselect/."""
    import soupselect
    soupselect.monkeypatch()

def to_soup(html_source):
    """Convert HTML source (text) to soup object."""
    return BeautifulSoup(html_source)

def prettify(soup):
    """Prettify HTML source. The HTML source is in a soup object."""
    return soup.prettify()

def doc_to_soup(doc):
    return to_soup(lx.tostring(doc))

# The patch is applied automatically when this module is imported.
css_patch()

#############################################################################

if __name__ == "__main__":
    url = "http://index.hu"
    text = web.get_page(url)
    soup = to_soup(text)
    print prettify(soup)