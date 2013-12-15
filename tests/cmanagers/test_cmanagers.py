import os
from jabbapylib.cmanagers.cmanagers import ChDir
from jabbapylib.filesystem import fs

TEST = "3694402219400478969.txt"

def test_chdir():
    tmp_file = os.path.join("/tmp", TEST)
    assert not os.path.isfile(tmp_file)
    with ChDir("/tmp"):
        fs.touch(TEST)
    assert os.path.isfile(tmp_file)
    os.unlink(tmp_file)
    assert not os.path.isfile(tmp_file)
    #
    assert not os.path.isfile(TEST)
    fs.touch(TEST)
    assert os.path.isfile(TEST)
    os.unlink(TEST)
    assert not os.path.isfile(TEST)
