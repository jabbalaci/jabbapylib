# -*- coding: utf-8 -*-

from jabbapylib.text import ascii


def test_remove_accents():
    assert ascii.remove_accents('László') == 'Laszlo'
    assert ascii.remove_accents('ünnep') == 'unnep'
    assert ascii.remove_accents('áéíóöőúüű') == 'aeiooouuu'
    assert ascii.remove_accents('ÁÉÍÓÖŐÚÜŰ') == 'AEIOOOUUU'

    
def test_remove_non_ascii():
    assert ascii.remove_non_ascii('László') == 'Lszl'
    assert ascii.remove_non_ascii('ünnep') == 'nnep'
    assert ascii.remove_non_ascii('áéíóöőúüű-ok') == '-ok'
    assert ascii.remove_non_ascii('ÁÉÍÓÖŐÚÜŰ-ok') == '-ok'