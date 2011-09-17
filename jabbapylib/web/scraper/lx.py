#!/usr/bin/env python

"""
Working with lxml.

HTML elements have all the methods that come with ElementTree, but also include 
some extra methods (see http://lxml.de/lxmlhtml.html, section HTML Element Methods).

Element: http://docs.python.org/library/xml.etree.elementtree.html#element-objects.
"""

from lxml import html


def to_doc(text):
    return html.document_fromstring(text)

def prettify(doc, method='xml'):
    """Method 'html' is not pretty at all."""
    return html.tostring(doc, pretty_print=True, method=method)

def flatten(doc):
    """Serialise to plain text without markup."""
    return html.tostring(doc, method='text')

#############################################################################

if __name__ == "__main__":
    text = """
<html>
    <table>
        <tr><td>Header</td></tr>
        <tr><td>Want This</td></tr>
    </table>
    <a href="http://google.ca">Google.ca</a>
</html>
"""
    doc = to_doc(text)
    row1 = doc.cssselect('table')[0]
    print row1.cssselect('tr td')[0].text