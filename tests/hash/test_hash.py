import os
from jabbapylib.hash import hash

FILE = '/tmp/jabbapylib.tmp'


def setup_module(module):
    f = open(FILE, 'w')
    print >>f, 'first line'
    print >>f, 'second line'
    f.close()
    
    
def teardown_module(module):
    os.unlink(FILE)
    
##########

class TestHash:
    
    def test_string_to_md5(self):
        assert hash.string_to_md5('uncrackable12') == '7e1f843673a0c8082378a0f7e6831c7b'
        
    def test_file_to_md5(self):
        res = hash.file_to_md5(FILE)
        assert res == '7565a01bd35f31ba82ab55c978c1b755'
        