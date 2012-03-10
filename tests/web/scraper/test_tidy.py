import scr_examples as ex
from jabbapylib.web.scraper import tidy

def test_pretty_print():
    res = tidy.pretty_print(ex.TIDY_IN)
    assert res == ex.TIDY_OUT