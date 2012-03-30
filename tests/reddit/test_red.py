import os
from jabbapylib.reddit import red


def test_credentials():
    assert os.path.isfile(red.USERNAME_TXT)
    assert os.path.isfile(red.PASSWORD_TXT)