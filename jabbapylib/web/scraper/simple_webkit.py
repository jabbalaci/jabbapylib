#!/usr/bin/env python

"""
Simple webkit.

Pro:
----
Evaluates embedded Javascript. 

Con:
----
It doesn't wait for all AJAX calls to finish. Actually, it cannot be known
when AJAX calls are finished. A possible solution is to make it wait somwhow
for X seconds, but I couldn't figure out how to do that. It's something with
QTimer. TODO: add this feature.

Another TODO: set a user-agent.
"""

import sys
from PyQt4 import QtGui, QtCore, QtWebKit


class SimpleWebkit():
    def __init__(self, url):
        self.url = url
        self.webView = QtWebKit.QWebView()
        
    def save(self):
        print self.webView.page().mainFrame().toHtml()
        sys.exit(0)
        
    def process(self):
        self.webView.load(QtCore.QUrl(self.url))
        QtCore.QObject.connect(self.webView, QtCore.SIGNAL("loadFinished(bool)"), self.save)


def process(url):
    app = QtGui.QApplication(sys.argv)
    
    s = SimpleWebkit(url)
    s.process()
    
    sys.exit(app.exec_())
    

#############################################################################

if __name__ == "__main__":
    #url = 'http://simile.mit.edu/crowbar/test.html'
    if len(sys.argv) > 1:
        process(sys.argv[1])
    else:
        print >>sys.stderr, "{0}: error: specify a URL.".format(sys.argv[0])
        sys.exit(1)