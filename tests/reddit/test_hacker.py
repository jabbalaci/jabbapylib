from jabbapylib.reddit import hacker


def test_get_random_title():
    res = hacker.get_random_title()
    assert len(res) > 0