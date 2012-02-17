import jabbapylib.config as cfg
from jabbapylib.process import process

URL = 'http://simile.mit.edu/crowbar/test.html'


def test_simple_webkit():
    cmd = "python {webkit} '{url}'".format(webkit=cfg.SIMPLE_WEBKIT, url=URL)
    
    text = process.get_simple_cmd_output(cmd)
    assert '<h1 id="message">Hi Crowbar!</h1>' in text
    # call it again:
    text = process.get_simple_cmd_output(cmd)
    assert '<h1 id="message">Hi Crowbar!</h1>' in text