import scr_examples as ex
from jabbapylib.lib.BeautifulSoup import BeautifulSoup
from jabbapylib.web.scraper import bs, lx


def test_css_patch():
    """Is it monkey-patched successfully?"""
    assert hasattr(BeautifulSoup, 'findSelect')    # same as below
    assert hasattr(BeautifulSoup, 'findCssSelect') # same as above


def test_to_soup():
    soup = bs.to_soup(ex.HTML_1)
    assert isinstance(soup, BeautifulSoup)
    assert str(soup) == """
<html>
<table>
<tr><td>Header</td></tr>
<tr><td>Want This</td></tr>
</table>
<a href="http://google.ca">Google.ca</a>
</html>
"""


def test_prettify():
    soup = bs.to_soup(ex.UGLY)
    assert soup.prettify() == """<html>
 <h1>
  Hello, World!
 </h1>
</html>"""


def test_doc_to_soup():
    doc = lx.to_doc(ex.HTML_1)
    soup = bs.doc_to_soup(doc)
    assert isinstance(soup, BeautifulSoup)
    
    
def test_get_links():
    soup = bs.to_soup(ex.LINKS)
    links = bs.get_links(soup, 'http://retrogames.com')
    assert links == ['http://retrogames.com', 'http://retrogames.com/games/elite', 'http://retrogames.com/games/commando']
    #
    links = bs.get_links(soup)
    assert links == ['http://retrogames.com', '/games/elite', '/games/commando']
    
    
def test_make_links_absolute():
    soup = bs.to_soup(ex.LINKS)
    soup = bs.make_links_absolute(soup, 'http://retrogames.com')
    #
    links = bs.get_links(soup)
    assert links == ['http://retrogames.com', 'http://retrogames.com/games/elite', 'http://retrogames.com/games/commando']
    