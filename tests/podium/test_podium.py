import re
from jabbapylib.podium import podium
from jabbapylib.filesystem import fs
import py.test


def test_get_hostname():
    assert podium.get_hostname()
    
def test_get_home_dir():
    username = podium.get_username()
    assert username in podium.get_home_dir()
    
def test_get_username():
    test_get_home_dir()
    
def test_is_linux():
    if fs.which('bash') == '/bin/bash':
        assert podium.is_linux()
        
def test_get_screen_resolution():
    result = podium.get_screen_resolution()
    assert len(result) == 2
    assert result[0] > 0 and result[1] > 0

def test_get_firefox_profile_folder():
    result = podium.get_firefox_profile_folder()
    assert re.search('.*/.{8}\.default$', result)

def test_get_fingerprint():
    assert len(podium.get_fingerprint()) > 0
    assert len(podium.get_fingerprint(md5=True)) == 32

def test_get_short_fingerprint():
    assert podium.get_fingerprint(md5=True) == podium.get_short_fingerprint(length=32)
    assert len(podium.get_short_fingerprint()) > 0
    py.test.raises(AssertionError, podium.get_short_fingerprint, 0)