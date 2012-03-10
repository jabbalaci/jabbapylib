import os
import re
import httplib

import jabbapylib.config as cfg
from jabbapylib.web import web

BITLY_URL = 'http://bit.ly/A6B9lT'
GOOGLE = 'http://google.com'
GOOGLE_HTML = ''
CROWBAR = 'http://simile.mit.edu/crowbar/test.html'


def setup_module(module):
    """runs just once per module"""
    global GOOGLE_HTML
    GOOGLE_HTML = web.get_page(GOOGLE)
    try:
        os.unlink(cfg.TEST_TMP_FILE)
    except:
        pass    # maybe it didn't exist
    
#############################################################################

def test_get_referer():
    assert web.get_referer('http://example.com/dir/file.html') == 'http://example.com'
    
def test_get_host():
    res = web.get_host('http://projecteuler.net/index.php?section=statistics')
    assert res == 'projecteuler.net'
    
def test_get_url_open():
    assert web.get_url_open(GOOGLE) is not None
    assert type(web.get_url_open(GOOGLE, user_agent=True, referer=True)) is not None
    
def test_get_url_info():
    res = web.get_url_info(GOOGLE)
    assert 'text/html' in res['Content-Type']
    
def test_get_redirected_url():
    assert web.get_redirected_url(BITLY_URL) == 'https://github.com/jabbalaci'
    
def test_get_server_status_code():
    assert web.get_server_status_code(BITLY_URL) == httplib.MOVED_PERMANENTLY    # 301
    print web.get_server_status_code(CROWBAR) == httplib.OK    # 200
    
def test_check_url():
    assert web.check_url('http://www.google.com')    # exists
    assert not web.check_url('http://simile.mit.edu/crowbar/nothing_here.html')    # doesn't exist
    
def test_get_page():
    assert '<title>Google</title>' in GOOGLE_HTML
       
def test_get_page_with_cookies_using_wget():
    assert web.get_page_with_cookies_using_wget(GOOGLE)

def test_get_page_with_cookies_using_cookiejar():
    assert web.get_page_with_cookies_using_cookiejar(GOOGLE)
    
def test_get_js_page():
    res = web.get_js_page(CROWBAR)
    assert '<h1 id="message">Hi Crowbar!</h1>' in res
    # can be called again:
    res = web.get_js_page(CROWBAR)
    assert '<h1 id="message">Hi Crowbar!</h1>' in res
    
def test_open_in_browser():
    tmp_file = web.open_in_browser(GOOGLE_HTML, test=True)
    assert re.search('^/tmp/tmp.*\.html$', tmp_file)
    os.unlink(tmp_file)
    
def test_html_to_text():
    res = web.html_to_text(GOOGLE_HTML, method=cfg.LYNX)
    assert 'Google' in res and 'References' in res
    #
    res = web.html_to_text(GOOGLE_HTML, method=cfg.HTML2TEXT)
    assert 'Google' in res
    #
    res = web.html_to_text(GOOGLE_HTML, method='unknown method')
    assert res is None
