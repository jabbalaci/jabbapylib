#!/usr/bin/env python

"""
Webkit.

source:
http://stackoverflow.com/questions/4003416/pyqt-save-dom-to-file
"""

import sys
from PyQt4 import QtGui, QtCore, QtWebKit

#url = 'http://simile.mit.edu/crowbar/test.html'
#url = 'http://dl.dropbox.com/u/144888/hello_js.html'
url = 'http://www.ncbi.nlm.nih.gov/nuccore/CP002059.1'
#url = 'https://dl.dropbox.com/u/144888/email_js.html'


class SimpleWebkit():
    def __init__(self, url, output):
        self.url = url
        self.output = output
        self.webView = QtWebKit.QWebView()
        
    def save(self):
        print self.webView.page().mainFrame().toHtml()
        sys.exit(0)
        
    def process(self):
        self.webView.load(QtCore.QUrl(self.url))
        QtCore.QObject.connect(self.webView, QtCore.SIGNAL("loadFinished(bool)"), self.save)


def main():
    app = QtGui.QApplication(sys.argv)
    
    s = SimpleWebkit(url)
    s.process()
    
    sys.exit(app.exec_())
    

#############################################################################

if __name__ == "__main__":
    main()