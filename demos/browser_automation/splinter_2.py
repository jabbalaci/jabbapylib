#!/usr/bin/env python

"""
splinter

http://splinter.cobrateam.info
"""

from time import sleep
from splinter.browser import Browser


#url = 'http://simile.mit.edu/crowbar/test.html'
#url = 'http://dl.dropbox.com/u/144888/hello_js.html'
url = 'http://www.ncbi.nlm.nih.gov/nuccore/CP002059.1'
#url = 'http://translate.google.com/#en|fr|game'

def main():
    #browser = Browser('zope.testbrowser')
    #browser = Browser('webdriver.chrome')
    browser = Browser()
    browser.visit(url)
    
    #browser.execute_script("var win = window.open(); win.document.write('<html><head><title>Generated HTML of  ' + location.href + '</title></head><pre>' + document.documentElement.innerHTML.replace(/&/g, '&amp;').replace(/</g, '&lt;') + '</pre></html>'); win.document.close(); void 0;")
    
    while 'ORIGIN' not in browser.html:
        sleep(5)
    
    f = open("/tmp/source.html", "w")
    print >>f, browser.html
    f.close()
    
    browser.quit()
    print '__END__'

#############################################################################

if __name__ == "__main__":
    main()