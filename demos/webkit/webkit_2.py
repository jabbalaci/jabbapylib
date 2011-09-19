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

class Sp():
    def save(self):
        print "call"
        #data = self.webView.page().currentFrame().documentElement().toInnerXml()
        #data = self.webView.page().mainFrame().documentElement().toInnerXml()
        data = self.webView.page().mainFrame().toHtml()
        open("w2.html","w").write(data)
        print 'finished'
        sys.exit(0)
    def main(self):
        self.webView = QtWebKit.QWebView()
        self.webView.load(QtCore.QUrl(url))
        QtCore.QObject.connect(self.webView,QtCore.SIGNAL("loadFinished(bool)"),self.save)


def main():
    app = QtGui.QApplication(sys.argv)
    s = Sp()
    s.main()
    sys.exit(app.exec_())


#############################################################################

if __name__ == "__main__":
    main()