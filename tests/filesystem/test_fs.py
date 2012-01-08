import os
import re
from jabbapylib.filesystem import fs

FILE = '/tmp/jabbapylib.tmp'

def setup_module(module):
    f = open(FILE, 'w')
    print >>f, 'first line'
    print >>f, 'second line'
    f.close()
    
def teardown_module(module):
    os.unlink(FILE)
    
##########
    
class TestFileSystem:
    
    def test_read_first_line(self):
        res = fs.read_first_line(FILE)
        assert res == 'first line'
        
    def test_is_local_path(self):
        assert fs.is_local_path(FILE)
        assert not fs.is_local_path('http://google.com')
        
    def test_get_timestamped_filename(self):
        res = fs.get_timestamped_filename()
        assert re.search('^\d{8}_\d{6}\.txt$', res)