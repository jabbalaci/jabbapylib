#!/usr/bin/env python

"""
Webkit.

source:
http://blog.motane.lu/2009/07/07/downloading-a-pages-content-with-python-and-webkit/
"""

import sys
import signal
 
from optparse import OptionParser
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from PyQt4.QtWebKit import QWebPage
 
 
class Crawler( QWebPage ):
    def __init__(self, url, file):
        QWebPage.__init__( self )
        self._url = url
        self._file = file
 
    def crawl( self ):
        signal.signal( signal.SIGINT, signal.SIG_DFL )
        self.connect( self, SIGNAL( 'loadFinished(bool)' ), self._finished_loading )
        self.mainFrame().load( QUrl( self._url ) )
 
    def _finished_loading( self, result ):
        file = open( self._file, 'w' )
        file.write( self.mainFrame().toHtml() )
        file.close()
        sys.exit( 0 )
 
def main():
    app = QApplication( sys.argv )
    options = get_cmd_options()
    crawler = Crawler( options.url, options.file )
    crawler.crawl()
    sys.exit( app.exec_() )
 
def get_cmd_options():
    """
        gets and validates the input from the command line
    """
    usage = "usage: %prog [options] args"
    parser = OptionParser(usage)
    parser.add_option('-u', '--url', dest = 'url', help = 'URL to fetch data from')
    parser.add_option('-f', '--file', dest = 'file', help = 'Local file path to save data to')
 
    (options,args) = parser.parse_args()
 
    if not options.url:
        print 'You must specify an URL.',sys.argv[0],'--help for more details' 
        exit(1)
    if not options.file:
        print 'You must specify a destination file.',sys.argv[0],'--help for more details'
        exit(1)
 
    return options

#############################################################################

if __name__ == "__main__":
    main()