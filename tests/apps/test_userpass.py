from jabbapylib.apps import userpass

def test_get_username():
    assert len(userpass.get_username(length=8)) == 8
    
def my_shuffle():
    array = [1,2,3]
    assert len(userpass.my_shuffle(array)[::-1]) == 3
    
def test_get_password():
    assert 5 <= len(userpass.get_password(min=5, max=10)) <= 10