from jabbapylib.podium.gnome.screensaver import screensaver
from jabbapylib.filesystem import fs


def test_screensaver():
    # TODO
    assert fs.which('gnome-screensaver-command') is not None