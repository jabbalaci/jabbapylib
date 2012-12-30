from jabbapylib.web.useragents import get_random_useragent

def test_get_random_useragent():
    res = get_random_useragent()
    assert res.startswith('Mozilla')
