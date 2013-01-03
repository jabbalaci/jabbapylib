from jabbapylib.web.useragents import get_useragents, get_random_useragent


def test_get_useragents():
    res = get_useragents()
    assert isinstance(res, list) and len(res) > 5

def test_get_random_useragent():
    res = get_random_useragent()
    assert res.startswith('Mozilla')
