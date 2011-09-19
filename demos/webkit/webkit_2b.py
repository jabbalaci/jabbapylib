#!/usr/bin/env python

"""
Webkit.

Trying to add sleep.

Some tips here: http://www.qtcentre.org/threads/21032-WebKit-accessing-javascript-results-googleMap
"""

import sys
import thread
from time import time, sleep
from PyQt4 import QtGui, QtCore, QtWebKit
#from PyQt4.QtCore import QTimer


url = 'http://simile.mit.edu/crowbar/test.html'
#url = 'http://dl.dropbox.com/u/144888/hello_js.html'
#url = 'http://www.ncbi.nlm.nih.gov/nuccore/CP002059.1'
#url = 'http://translate.google.com/#en|fr|game'

WAIT = 10

class Sp():
    def __init__(self):
        self.webView = QtWebKit.QWebView()
        
    def load_page(self):
        self.webView.load(QtCore.QUrl(url))
        
    def save(self):
        print "call"
        #data = self.webView.page().currentFrame().documentElement().toInnerXml()
        #data = self.webView.page().mainFrame().documentElement().toInnerXml()
        data = self.webView.page().mainFrame().toHtml()
        open("w2b.html","w").write(data)
        print 'finished'
        sys.exit(0)
        
    def register_save(self):
        QtCore.QObject.connect(self.webView, QtCore.SIGNAL("loadFinished(bool)"), self.save)
        #QtCore.QObject.connect(self.webView, QtCore.SIGNAL("loadFinished(bool)"), self, QtCore.SLOT("examineWait(bool)"))
        
    def examineWait(self, ok):
        QTimer.singleShot(5000, self, QtCore.SLOT("examinePage()"))
        
    def examinePage(self):
        return True


def main():
    app = QtGui.QApplication(sys.argv)
    
    s = Sp()
    s.load_page()
    s.register_save()
    
    sys.exit(app.exec_())


#############################################################################

if __name__ == "__main__":
    main()