from jabbapylib.network.ping import ping

def test_ping():
    assert ping('www.google.com') > 0.0