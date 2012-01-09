from jabbapylib.hash import hash
import jabbapylib.config as cfg

FILE = cfg.TEST_ASSETS_DIR + '/text.txt'


class TestHash:
    
    def test_string_to_md5(self):
        assert hash.string_to_md5('uncrackable12') == '7e1f843673a0c8082378a0f7e6831c7b'
        
    def test_file_to_md5(self):
        res = hash.file_to_md5(FILE)
        assert res == '7565a01bd35f31ba82ab55c978c1b755'
        