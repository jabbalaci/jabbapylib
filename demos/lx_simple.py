#!/usr/bin/env python

"""
Working with lxml.

HTML elements have all the methods that come with ElementTree, but also include 
some extra methods (see http://lxml.de/lxmlhtml.html, section HTML Element Methods).

Element: http://docs.python.org/library/xml.etree.elementtree.html#element-objects.
"""

from jabbapylib.web.scraper import lx, scraper
from jabbapylib.web.web import get_page


def demo1():
    text = """
<html>
    <table>
        <tr><td>Header</td></tr>
        <tr><td>Want This</td></tr>
    </table>
    <a href="http://google.ca">Google.ca</a>
</html>
"""
    doc = lx.to_doc(text)
    row1 = doc.cssselect('table')[0]
    print row1.cssselect('tr td')[0].text
    print doc.cssselect('a[href]')[0].get('href')
    
    
def demo2():
    url = 'http://projecteuler.net/'
    text = get_page(url)
    doc = lx.to_doc(text)
    lx.make_links_absolute(doc, base_url=url)
    print lx.tostring(doc)


def demo3():
    html = '''<html>
  <head>
    <script type="text/javascript" src="stuff.js"></script>
    <link rel="alternate" type="text/rss" src="some-rss">
    <style>
        body {background-image: url(javascript:do_something)};
        div {color: expression(something)};
    </style>
  </head>
  <body onload="some_function()">
     Hello World!
  </body>
 </html>'''
    doc = lx.to_doc(html)
    print lx.prettify(doc, method=scraper.BEAUTIFULSOUP)
    
def demo4():
    text = """
<html>
    <table>
        <tr><td>http://google.ca</td></tr>
        <tr><td>http://reddit.com</td></tr>
    </table>
</html>
"""
    doc = lx.to_doc(text)
    doc = lx.autolink(doc)
    print lx.prettify(doc)
    
def demo5():
    text = """
<html>
    <table>
        <tr><td>http://google.ca</td></tr>
        <tr><td>http://reddit.com</td></tr>
    </table>
</html>
"""
    doc = lx.to_doc(text)
    lx.show_paths(doc)
    

#############################################################################

if __name__ == "__main__":
    #demo1()
    #demo2()
    #demo3()
    #demo4()
    #demo5()
    pass
