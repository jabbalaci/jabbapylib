# Here I make the following assumptions:
# (1) you use Firefox, and
# (3) you have at least one cookie stored in cookies.sqlite

import os
import cookielib
from jabbapylib import config as cfg
from jabbapylib.web import export_firefox_cookies as efc

HOST = ''    # any host


def test_cookie_db():
    assert os.path.exists(cfg.COOKIE_DB)
    
def test_get_cookies_in_text():
    test_cookie_db()
    #
    res = efc.get_cookies_in_text(HOST)
    assert res
    
    
def test_get_cookies_in_cookiejar():
    test_cookie_db()
    #
    res = efc.get_cookies_in_cookiejar(HOST)
    assert isinstance(res, cookielib.LWPCookieJar)
    #assert res.__class__.__name__ == 'LWPCookieJar'
    assert len(res) > 0    # we have at least one cookie
