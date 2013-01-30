from jabbapylib.podium.gnome.screensaver import screensaver
from jabbapylib.filesystem import fs


def test_screensaver():
    # TODO
    assert fs.which('gnome-screensaver-command') is not None

def test_lock_screen():
    # TODO
    assert fs.which('gnome-screensaver-command') is not None

def test_unlock_screen():
    # TODO
    assert fs.which('gnome-screensaver-command') is not None