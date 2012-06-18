from jabbapylib.network import geoinfo

def test_geo():
    ip = '173.194.35.177'    # Google
    host = geoinfo.Host(ip)
    assert host.get_country_code() == 'US'