#!/usr/bin/env python

"""
Three different parsers.
"""

from jabbapylib.web.scraper import lx
from jabbapylib.web.scraper import scraper

text = "<table><td>foo"

def demo1():
    doc = lx.to_doc(text)
    print lx.prettify(doc)

def demo2():
    doc = lx.to_doc(text, parser=scraper.HTML5PARSER)
    print lx.prettify(doc)

def demo3():
    doc = lx.to_doc(text, parser=scraper.SOUPPARSER)
    print lx.prettify(doc)

#############################################################################

if __name__ == "__main__":
    demo1()
    #demo2()
    demo3()
