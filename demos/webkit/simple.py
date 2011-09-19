#!/usr/bin/env python

"""
Webkit.

source:
http://blog.motane.lu/2009/06/18/pywebkitgtk-execute-javascript-from-python/
"""

import gtk #@UnresolvedImport
import webkit
 
url = 'http://www.google.com'

def main():
    window = gtk.Window()
    view = webkit.WebView()
    view.open(url)
    window.add(view)
    window.show_all()
    window.connect('delete-event', lambda window, event: gtk.main_quit())
     
    gtk.main()

#############################################################################

if __name__ == "__main__":
    main()