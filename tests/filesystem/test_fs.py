import re
from jabbapylib.filesystem import fs
import jabbapylib.config as cfg

FILE = cfg.TEST_ASSETS_DIR + '/text.txt'

    
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
