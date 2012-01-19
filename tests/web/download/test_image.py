import os
import shutil
import jabbapylib.config as cfg
from jabbapylib.web.download import image
from jabbapylib.filesystem import fs

img = None

def setup_module(module):
    """runs just once per module"""
    global img
    pic = 'http://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Bodiam-castle-10My8-1197.jpg/300px-Bodiam-castle-10My8-1197.jpg'
    img = image.Image(cfg.TMP_DIR, '2012-01-19', pic)
    #
    d = img.get_local_dir()
    if os.path.exists(d):
        shutil.rmtree(d)
        
        
def teardown_module(module):
    """runs once when all tests in this module are executed"""
    if os.path.exists(cfg.TMP_DIR):
        shutil.rmtree(cfg.TMP_DIR)
    
#############################################################################

def test_get_file_name():
    res = img.get_file_name()
    assert res == '300px-Bodiam-castle-10My8-1197.jpg'
    
def test_get_local_dir():
    res = img.get_local_dir()
    assert res == '{dir}/2012-01-19'.format(dir=cfg.TMP_DIR)
    
def test_get_local_path():
    res = img.get_local_path()
    assert res == '{dir}/2012-01-19/300px-Bodiam-castle-10My8-1197.jpg'.format(dir=cfg.TMP_DIR)
    
def test_get_skip_path():
    res = img.get_skip_path()
    assert res == '{dir}/2012-01-19/skip'.format(dir=cfg.TMP_DIR)
    
def test_exists_1():
    assert fs.remove_file_silently(img.get_local_path())
    assert img.exists() is False
    
def test_make_dirs():
    d = img.get_local_dir()
    #
    if os.path.exists(d):
        shutil.rmtree(d)
    #
    assert not os.path.exists(d)
    assert img.make_dirs()
    assert os.path.exists(d)
    os.rmdir(d)
    assert not os.path.exists(d)
    
def test_get_readme_path():
    res = img.get_readme_path()
    assert res == '{dir}/2012-01-19/README'.format(dir=cfg.TMP_DIR)
    
def test_save_readme():
    assert img.make_dirs()
    #
    text = """readme 1st line
readme 2nd line"""
    img.readme = text
    assert not os.path.exists(img.get_readme_path())
    img.save_readme()
    line = fs.read_first_line(img.get_readme_path())
    assert line == 'readme 1st line'
    os.unlink(img.get_readme_path())
    assert not os.path.exists(img.get_readme_path())
    
def test_download():
    d = img.get_local_dir()
    #
    assert img.download()
    assert os.path.exists(img.get_local_path()) 
    shutil.rmtree(d)
    #
    img.make_dirs()
    fs.touch(os.path.join(d, image.SKIP))
    assert img.download() is False
    assert not os.path.exists(img.get_local_path())
