import re
from jabbapylib.platform import platform
from jabbapylib.filesystem import fs

def test_get_hostname():
    assert platform.get_hostname()
    
def test_get_home_dir():
    username = platform.get_username()
    assert username in platform.get_home_dir()
    
def test_get_username():
    test_get_home_dir()
    
def test_is_linux():
    if fs.which('bash') == '/bin/bash':
        assert platform.is_linux()
        
def test_get_screen_resolution():
    result = platform.get_screen_resolution()
    assert len(result) == 2
    assert result[0] > 0 and result[1] > 0

def test_get_firefox_profile_folder():
    result = platform.get_firefox_profile_folder()
    assert re.search('.*/.{8}\.default$', result)