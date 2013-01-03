from jabbapylib.web.scraper import jabba_webkit as jw

URL = 'http://simile.mit.edu/crowbar/test.html'


def test_simple_webkit():
    assert '<h1 id="message">Hi Crowbar!</h1>' in jw.get_page(URL)
    # call it again:
    assert '<h1 id="message">Hi Crowbar!</h1>' in jw.get_page(URL)