#!/usr/bin/env python

"""
Some constants.
"""

import time
import random as r


LXML_HTML = 'lxml.html'
HTML5PARSER = 'lxml.html.html5parser'
BEAUTIFULSOUP = 'lxml.html.soupparser or BeautifulSoup'
TIDY = 'tidy'


def sleep(fix=5, plus=5):
    """Sleep for some randomized time.
    
    Time will be a real value between fix and fix+plus."""
    sec = fix + r.uniform(0, plus)
    #print sec
    time.sleep(sec)


#############################################################################

if __name__ == "__main__":
    for i in range(5):
        sleep()