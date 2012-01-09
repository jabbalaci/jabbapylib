import re
from jabbapylib.mouse import mousepos


def test_mousepos():
    res = str(mousepos.mousepos())
    assert re.search('\(\d+, \d+\)', res)