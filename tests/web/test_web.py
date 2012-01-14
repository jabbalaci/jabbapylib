from jabbapylib.web import web


def test_get_referer():
    assert web.get_referer('http://example.com/dir/file.html') == 'http://example.com'
    
def test_get_host():
    res = web.get_host('http://projecteuler.net/index.php?section=statistics')
    assert res == 'projecteuler.net'