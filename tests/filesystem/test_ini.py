import re
from jabbapylib.platform import platform
from jabbapylib.filesystem import ini

def test_read_ini():
    ini_file = '{home}/.mozilla/firefox/profiles.ini'.format(home=platform.get_home_dir())
    path = ini.read_ini('Profile0', ini_file)['path']
    assert re.search('.{8}\.default', path)