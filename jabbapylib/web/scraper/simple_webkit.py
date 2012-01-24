#!/usr/bin/env python

"""
Simple webkit.

based on: http://blog.sitescraper.net/2010/06/scraping-javascript-webpages-in-python.html 

Pro:
----
Evaluates embedded Javascript. 

Con:
----
It doesn't wait for all AJAX calls to finish. Actually, it cannot be known
when AJAX calls are finished. A possible solution is to make it wait somewhow
for X seconds, but I couldn't figure out how to do that. It's something with
QTimer. TODO: add this feature.

Another TODO: set a user-agent.

# from jabbapylib.web.scraper import simple_webkit
"""

import sys

from PyQt4.QtGui import QApplication
from PyQt4.QtWebKit import QWebPage
from PyQt4.QtCore import QUrl


class SimpleWebkit(QWebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.save)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()
        
    def save(self):
        self.html = self.mainFrame().toHtml()
        self.app.quit()


def get_html(url):   
    s = SimpleWebkit(url)
    return str(s.html)      # QString to string !

#############################################################################

if __name__ == "__main__":
    url = 'http://simile.mit.edu/crowbar/test.html'
    print get_html(url)     # OK
    print '=========='
    print get_html(url)     # never called :(
    
#    if len(sys.argv) > 1:
#        get_html(sys.argv[1])
#    else:
#        print >>sys.stderr, "{0}: error: specify a URL.".format(sys.argv[0])
#        sys.exit(1)
