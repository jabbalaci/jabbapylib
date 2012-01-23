import os
import re
from jabbapylib.filesystem import fs
import jabbapylib.config as cfg
from jabbapylib.web import web

GOOGLE = 'http://google.com'
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
        
    def test_remove_file_silently(self):
        fname = '/stupid_directory_name/doesnt_exist.txt'
        assert fs.remove_file_silently(fname)
        assert fs.touch(cfg.TMP_FILE)
        assert os.path.exists(cfg.TMP_FILE)
        assert fs.remove_file_silently(cfg.TMP_FILE)
        
    def test_touch(self):
        assert fs.remove_file_silently(cfg.TMP_FILE)
        #
        assert fs.touch(cfg.TMP_FILE)
        assert os.path.exists(cfg.TMP_FILE)
        #
        assert fs.remove_file_silently(cfg.TMP_FILE)
        assert fs.touch(cfg.TMP_FILE, mode=0644)
        assert fs.get_oct_mode(cfg.TMP_FILE) == '0644'
        #
        assert fs.remove_file_silently(cfg.TMP_FILE)
        
    def test_get_oct_mode(self):
        assert fs.remove_file_silently(cfg.TMP_FILE)
        #
        assert fs.touch(cfg.TMP_FILE, mode=0755)
        assert fs.get_oct_mode(cfg.TMP_FILE) == '0755'
        #
        assert fs.remove_file_silently(cfg.TMP_FILE)
        
    def test_set_mode_to(self):
        assert fs.remove_file_silently(cfg.TMP_FILE)
        #
        assert fs.touch(cfg.TMP_FILE, mode=0600)
        assert fs.get_oct_mode(cfg.TMP_FILE) == '0600'
        assert fs.set_mode_to(cfg.TMP_FILE, 0755)
        assert fs.set_mode_to(cfg.TMP_FILE, 0700)
        #
        assert fs.remove_file_silently(cfg.TMP_FILE)
        
    def test_store_content_in_file(self):
        content = web.get_page(GOOGLE)
        assert not os.path.exists(cfg.TEST_TMP_FILE)
        fs.store_content_in_file(content, cfg.TEST_TMP_FILE)
        assert os.path.getsize(cfg.TEST_TMP_FILE) > 0
        os.unlink(cfg.TEST_TMP_FILE)
        