import re
from jabbapylib.podium import podium
from jabbapylib.filesystem import ini

def test_read_ini():
    ini_file = '{home}/.mozilla/firefox/profiles.ini'.format(home=podium.get_home_dir())
    path = ini.read_ini('Profile0', ini_file)['path']
    assert re.search('.{8}\.default', path)