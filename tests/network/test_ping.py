from jabbapylib.network.ping import ping, fping

def test_ping():
    assert ping('www.google.com') > 0.0

def test_fping():
    assert fping('www.google.com') > 0.0