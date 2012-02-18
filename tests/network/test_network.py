import re
from jabbapylib.network import network

IP = None

def setup_module(module):
    """runs just once per module"""
    global IP
    IP = network.get_my_external_ip()
    
#############################################################################

def test_is_internet_on():
    if IP:
        assert network.is_internet_on()
    else:
        assert not network.is_internet_on()

def test_get_my_external_ip():
    if IP:
        assert re.search('^\d+\.\d+\.\d+\.\d+$', IP)
    else:
        assert IP is None