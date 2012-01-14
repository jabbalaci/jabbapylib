# Well, it's not sure you have any cookies at all.
# So I make here just a simple test.

import os
from jabbapylib.web import export_firefox_cookies as efc


def test_cookie_db():
    assert os.path.exists(efc.COOKIE_DB)