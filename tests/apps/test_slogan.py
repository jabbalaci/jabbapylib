from jabbapylib.apps import slogan

def test_get_slogan():
    assert 'Python' in slogan.get_slogan('Python')[0]
