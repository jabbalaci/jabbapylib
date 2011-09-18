#!/usr/bin/env python

"""
Working with lxml.

HTML elements have all the methods that come with ElementTree, but also include 
some extra methods (see http://lxml.de/lxmlhtml.html, section HTML Element Methods).

Element: http://docs.python.org/library/xml.etree.elementtree.html#element-objects.

html.tostring: not pretty
etree.tostring: pretty
"""

import sys

import bs
import scraper
import tidy

from lxml import html
from lxml import cssselect
from lxml import etree
#from lxml.html import html5parser
from lxml.html import soupparser
from lxml.html import clean

import html5lib
from html5lib import treebuilders


def to_doc(text, parser=scraper.LXML_HTML, whole_doc=True):
    """Parse an HTML text.
    
    parser: which parser to use. 
    whole_doc: parse to complete HTML document (with <html> around), or parse just a fragment of HTML."""
    doc = None
    
    if parser == scraper.LXML_HTML:
        if whole_doc:
            doc = html.document_fromstring(text)
        else:
            doc = html.fromstring(text)
    elif parser == scraper.HTML5PARSER:
        # html5parser was broken for me, bug report is here: https://bugs.launchpad.net/lxml/+bug/780642
        #if whole_doc:
        #    doc = html5parser.document_fromstring(text)
        #else:
        #    doc = html5parser.fromstring(text)
        # Here is my workaround:
        parser = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder("lxml"), namespaceHTMLElements=False)
        doc = parser.parse(text)
    elif parser == scraper.SOUPPARSER:
        # soupparser has no document_fromstring method
        doc = soupparser.fromstring(text)
    else:
        print >>sys.stderr, "Error: you want to use an unknown parser in lx.py."
        # doc is None
        
    return doc


def prettify(doc, method=scraper.LXML_HTML):
    """Pretty print HTML."""
    text = None
    
    if method == scraper.LXML_HTML:                     # not so pretty
        text = html.tostring(doc, pretty_print2=True)
    elif method == scraper.BEAUTIFULSOUP:               # pretty
        soup = bs.doc_to_soup(doc)
        text = bs.prettify(soup)
    elif method == scraper.TIDY:
        text = tidy.pretty_print(tostring(doc))
    else:
        print >>sys.stderr, "Error: you want to use an unknown method in lx.py."
        # text is None
        
    return text


def flatten(doc):
    """Serialise to plain text without markup."""
    return html.tostring(doc, method='text')


def tostring(doc):
    """Convert an element to html."""
    return html.tostring(doc)


def make_links_absolute(doc, base_url):
    """Replace relative links with absolute links."""
    doc.make_links_absolute(base_url)
    return doc


def autolink(doc):
    """Replace http:// strings (texts) with HTML links.
    
    See http://lxml.de/lxmlhtml.html, section autolink."""
    clean.autolink(doc)
    return doc


def css_to_xpath(css):
    """CSS to XPath.
    
    Example: css_to_xpath('div.pad a')."""
    return cssselect.css_to_xpath(css)


def show_paths(doc):
    """Show paths of HTML texts."""
    tree = etree.ElementTree(doc)
    for e in tree.iter():
        if e.text:
            print "'{0}' => {1}".format(e.text, tree.getpath(e))

#############################################################################

if __name__ == "__main__":
    pass
