from jabbapylib.distance.dist import lev_dist, ham_dist, similarity

def test_lev_dist():
    assert lev_dist('ag-tcc', 'cgctca') == 3
    assert lev_dist('GUMBO', 'GAMBOL') == 2
    assert lev_dist('Google', 'Yahoo!') == 6
    
def test_ham_dist():
    assert ham_dist('toned', 'roses') == 3
    
def test_similarity():
    assert similarity('toned', 'roses') == 2