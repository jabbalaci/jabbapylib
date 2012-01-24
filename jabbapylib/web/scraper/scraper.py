#!/usr/bin/env python

"""
Some constants.

# from jabbapylib.web.scraper import scraper
"""

import time
import random as r


LXML_HTML = 'lxml.html'
HTML5PARSER = 'lxml.html.html5parser'
BEAUTIFULSOUP = 'lxml.html.soupparser or BeautifulSoup'
TIDY = 'tidy'


def sleep(fix=5, plus=5, test=False):
    """Sleep for some randomized time.
    
    Time will be a real value between fix and fix+plus."""
    sec = fix + r.uniform(0, plus)
    #print sec
    if not test:
        time.sleep(sec)
        
    return sec


#############################################################################

if __name__ == "__main__":
    for i in range(5):
        print sleep()
