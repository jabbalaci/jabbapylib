import sys
from cStringIO import StringIO
from jabbapylib.say import hello


def test_hi():
    buf = StringIO()
    old_stdout = sys.stdout
    sys.stdout = buf
    hello.hi()
    assert buf.getvalue() == 'jabbapylib works :)\n'
    buf.close()
    sys.stdout = old_stdout