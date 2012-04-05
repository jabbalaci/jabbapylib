import os
from jabbapylib.say import say

def test_say_with_google():
    good = 'python'
    assert say.say_with_google(good, autoremove=True, debug=True) == (True, None)
    assert say.say_with_google(good, autoremove=False, debug=True) == (True, '/tmp/python.mp3')
    os.unlink('/tmp/python.mp3')
    #
    bad = 'too long'
    assert say.say_with_google(bad, autoremove=True, debug=True) == (False, None)
    assert say.say_with_google(bad, autoremove=False, debug=True) == (False, None)