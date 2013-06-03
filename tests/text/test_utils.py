# -*- coding: utf-8 -*-

from jabbapylib.text import utils


def test_inc_string():
    assert utils.inc_string('a') == 'b'
    assert utils.inc_string('f') == 'g'
    assert utils.inc_string('z') == 'aa'
    assert utils.inc_string('zz') == 'aaa'
    assert utils.inc_string('af') == 'ag'
    assert utils.inc_string('ajhfsdhgf') == 'ajhfsdhgg'
    assert utils.inc_string('ajhfsdhgz') == 'ajhfsdhha'
