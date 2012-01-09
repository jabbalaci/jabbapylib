from jabbapylib.say import hyphen


def test_hyphen():
    word = 'python'
    res = hyphen.process(word)
    assert res[0] == 'python'
    assert res[1] == 'py-thon'
    assert res[2] == 'http://sp.dictionary.com/dictstatic/dictionary/audio/luna/P09/P0975800.mp3'