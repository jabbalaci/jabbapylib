#!/usr/bin/env python

"""
Check the latest stable version of mc.
"""

URL = 'http://www.midnight-commander.org/downloads'

import re
import urllib2
from BeautifulSoup import BeautifulSoup


def main():
    text = urllib2.urlopen(URL).read()
    soup = BeautifulSoup(text)
    for tag in soup.findAll('div', {'class': 'description'}):
        desc = tag.text
        result = re.search('^(Midnight Commander v.*\(stable release\))', desc)
        if result:
            latest = result.group(1)
            
    print latest

#############################################################################

if __name__ == "__main__":
    main()