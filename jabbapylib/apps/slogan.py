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
    assert 1 <= times <= 10     # be nice with the server
    #
    li = []
    url = BASE + urllib.urlencode({'user' : word})
    for _ in xrange(times):
        text = get_page(url, user_agent=True)
        soup = bs.to_soup(text)
        slogan = soup.findCssSelect('html body div p')[0].text
        if string.count(slogan, '.') == 1 and not slogan[0].isupper():
            slogan = slogan.replace('.', '')
        if len(slogan) >= 2 and slogan[-1] == '.' and slogan[-2] == '!':
            slogan = slogan[:-1]
        li.append(slogan)
        
    return li

#############################################################################

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print >>sys.stderr, 'Error: specify a keyword.'
        sys.exit(1)
    # else
    word = sys.argv[1]
    times = 5
    try:
        times = int(sys.argv[2])
    except:
        pass
    for s in get_slogan(word, times):
        print s
