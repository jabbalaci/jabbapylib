from jabbapylib.apps import imdb

def test_Movie():
    m = imdb.Movie('fight club')
    assert m['Year'] == '1999'
    
def test_get_rating():
    assert imdb.get_rating('star wars episode 4') >= 8.0