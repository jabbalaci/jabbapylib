import os
from jabbapylib.math import pi

def test_get_digits_of():
    digits = pi.get_digits_of(pi.PI3)
    assert len(digits) == 1000
    assert digits[:10] == '1415926535'
    assert digits[-10:] == '2164201989'
    os.unlink(pi.TMP_DIR + '/' + pi.PI3)