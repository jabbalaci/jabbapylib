#!/usr/bin/env python

"""
A simple scraper for http://sloganmaker.com/sloganmaker.php .

# from jabbapylib.apps.slogan import slogan
"""

import sys
import urllib
import string
from jabbapylib.web.scraper import bs
from jabbapylib.web.web import get_page

BASE = 'http://sloganmaker.com/sloganmaker.php?'

def get_slogan(word, times=1):
    assert times <= 10
    #
    li = []
    url = BASE + urllib.urlencode({'user' : word})
    for _ in xrange(times):
        text = get_page(url, user_agent=True)
        soup = bs.to_soup(text)
        slogan = soup.findCssSelect('html body div p')[0].text
        if string.count(slogan, '.') == 1 and not slogan[0].isupper():
            slogan = slogan.replace('.', '')
        li.append(slogan)
        
    return li

#############################################################################

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print >>sys.stderr, 'Error: specify a keyword.'
        sys.exit(1)
    # else
    for s in get_slogan(sys.argv[1], times=5):
        print s
