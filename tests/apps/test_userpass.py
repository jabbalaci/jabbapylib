from jabbapylib.apps import userpass

def test_get_username():
    name = userpass.get_username(length=8)
    assert name.islower() and name.isalpha()
    assert len(name) == 8
    
def my_shuffle():
    array = [1,2,3]
    assert len(userpass.my_shuffle(array)[::-1]) == 3
    
def test_get_password():
    passwd = userpass.get_password(min=5, max=10)
    assert passwd.isalnum()
    assert 5 <= len(passwd) <= 10

def test_get_urandom_password():
    passwd = userpass.get_urandom_password(min=5, max=10)
    assert passwd.isalnum()
    assert 5 <= len(passwd) <= 10