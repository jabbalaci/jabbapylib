import re
from jabbapylib.apps import bing

def test_extract():
    img_url, save_name = bing.extract(test=True)
    assert 'www.bing.com' in img_url
    #
    assert re.search('^\d{4}_\d\d_\d\d\-.*$', save_name)