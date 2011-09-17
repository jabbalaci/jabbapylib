#!/usr/bin/env python

"""
Working with lxml and html5lib.
"""

import html5lib
from html5lib import treebuilders

from jabbapylib.web.scraper import lx, scraper


def demo1():
    text = "<table><td>foo"
    parser = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder("lxml"), namespaceHTMLElements=False)
    doc = parser.parse(text)
    print lx.prettify(doc, method=scraper.BEAUTIFULSOUP)
     

#############################################################################

if __name__ == "__main__":
    demo1()
    pass
