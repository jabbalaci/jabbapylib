import sys
import lxml.html
import scr_examples as ex
from jabbapylib.web.scraper import lx, scraper
from cStringIO import StringIO
import html5lib
from html5lib import treebuilders
from lxml import html


def test_to_doc():
    #doc = lx.to_doc(ex.HTML_1)    # could be this too
    doc = lx.to_doc(ex.HTML_1, scraper.LXML_HTML)    # this parser is the default
    assert isinstance(doc, lxml.html.HtmlElement)
    #
    doc = lx.to_doc(ex.HTML_1, scraper.HTML5PARSER)
    assert isinstance(doc, lxml.html.HtmlElement)
    #
    doc = lx.to_doc(ex.HTML_1, scraper.BEAUTIFULSOUP)
    assert isinstance(doc, lxml.html.HtmlElement)
    #
    doc = lx.to_doc(ex.HTML_1, parser=None)
    assert doc is None
    #
    # now let's see with HTML fragments
    #
    doc = lx.to_doc(ex.FRAGMENT, scraper.LXML_HTML, whole_doc=False)
    assert isinstance(doc, lxml.html.HtmlElement)
    #
    doc = lx.to_doc(ex.FRAGMENT, scraper.HTML5PARSER, whole_doc=False)
    assert isinstance(doc, lxml.html.HtmlElement)
    #
    doc = lx.to_doc(ex.FRAGMENT, scraper.BEAUTIFULSOUP, whole_doc=False)
    assert isinstance(doc, lxml.html.HtmlElement)
    #
    doc = lx.to_doc(ex.FRAGMENT, parser=None, whole_doc=False)
    assert doc is None
    
    
def test_prettify():
    doc = lx.to_doc(ex.UGLY, parser=scraper.LXML_HTML)
    #
    nice = lx.prettify(doc, method=scraper.LXML_HTML)
    assert '</h1>' in nice and '</html>' in nice
    #
#    nice = lx.prettify(doc, method=scraper.HTML5PARSER)    # missing
    #
    nice = lx.prettify(doc, method=scraper.BEAUTIFULSOUP)
    assert '</h1>' in nice and '</html>' in nice
    #
    nice = lx.prettify(doc, method=scraper.TIDY)
    assert '</h1>' in nice and '</html>' in nice
    #
    nice = lx.prettify(doc, method=None)
    assert nice is None
    
    
def test_flatten():
    doc = lx.to_doc(ex.HTML_1)
    assert lx.flatten(doc) == 'HeaderWant ThisGoogle.ca\n'
    
    
def test_tostring():
    doc = lx.to_doc(ex.HTML_1)
    html = lx.tostring(doc)
    assert type(html) is str and len(html) > 0
    
    
def test_make_links_absolute():
    doc = lx.to_doc(ex.LINKS)
    doc = lx.make_links_absolute(doc, base_url='http://retrogames.com')
    html = lx.tostring(doc)
    assert "http://retrogames.com/games/elite" in html
    assert "http://retrogames.com/games/commando" in html
    
    
def test_autolink():
    doc = lx.to_doc(ex.TEXT)
    doc = lx.autolink(doc)
    html = lx.tostring(doc)
    assert '<a href="http://retrogames.com/games/commando">http://retrogames.com/games/commando</a>' in html
    
    
def test_css_to_xpath():
    assert lx.css_to_xpath('tr td') == '//tr//td'
    assert lx.css_to_xpath('a[href]') == '//a[@href]'
    
    
def test_show_paths():
    doc = lx.to_doc(ex.HTML_1)
    
    old_stdout = sys.stdout
    buf = StringIO()
    sys.stdout = buf 
    #
    lx.show_paths(doc, find=None)
    assert "'Want This' => /html/body/table/tr[2]/td" in buf.getvalue()
    #
    buf = StringIO()
    sys.stdout = buf
    lx.show_paths(doc, find='Google.ca')
    assert "'Google.ca' => /html/body/a" in buf.getvalue()
    #
    buf.close()
    sys.stdout = old_stdout
    
    
def test_open_in_browser():
    pass


def test_elementtree_to_string():
    parser = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder("lxml"), namespaceHTMLElements=False)
    etree_doc = parser.parse(ex.HTML_1)  # returns an ElementTree
    assert '<tbody><tr><td>Header</td></tr>' in lx.elementtree_to_string(etree_doc)
