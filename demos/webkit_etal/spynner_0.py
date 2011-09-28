#!/usr/bin/env python

"""
spynner

https://github.com/rndbit/spynner

a fork: https://bitbucket.org/leapfrogdevelopment/punkybrowster
"""

import spynner

url = 'http://simile.mit.edu/crowbar/test.html'
#url = 'http://dl.dropbox.com/u/144888/hello_js.html'
#url = 'http://www.ncbi.nlm.nih.gov/nuccore/CP002059.1'
#url = 'https://dl.dropbox.com/u/144888/email_js.html'

def main():
    browser = spynner.Browser()
    browser.load(url)
    #while 'ORIGIN' not in browser.html:
    #    browser.wait(3)
    print browser.html
    #print len(browser.html)

#############################################################################

if __name__ == "__main__":
    main()