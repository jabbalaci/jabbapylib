#!/usr/bin/env python

"""
Three different parsers.
"""

from jabbapylib.web.scraper import lx
from jabbapylib.web.scraper import scraper

text = "<table><td>foo"

def demo1():
    doc = lx.to_doc(text)
    print lx.prettify(doc, method=scraper.BEAUTIFULSOUP)

def demo2():
    doc = lx.to_doc(text, parser=scraper.HTML5PARSER)
    print lx.prettify(doc, method=scraper.BEAUTIFULSOUP)

def demo3():
    doc = lx.to_doc(text, parser=scraper.BEAUTIFULSOUP)
    print lx.prettify(doc, method=scraper.BEAUTIFULSOUP)

#############################################################################

if __name__ == "__main__":
    demo1()
    print '-'*40
    demo2()
    print '-'*40
    demo3()
