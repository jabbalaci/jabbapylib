import os
import glob
from jabbapylib.multimedia import video
import jabbapylib.config as cfg

FILE = cfg.TEST_ASSETS_DIR + '/video.avi'


def test_get_video_info():
    res = video.get_video_info(FILE)
    assert type(res) is dict and res.has_key('ID_VIDEO_FPS')

    
def test_get_video_length():
    assert video.get_video_length(FILE) == 5.02

    
def test_get_video_summary():
    res = video.get_video_summary(FILE)
    assert res == 'VIDEO:  [MP4V]  854x480  24bpp  23.976 fps    0.0 kbps ( 0.0 kbyte/s)'

    
def test_make_screenshot():
    res = video.make_screenshot(FILE, 4, outdir=cfg.TEST_TMP_DIR)
    ss_file = cfg.TEST_TMP_DIR + '/' + video.MPLAYER_SCREENSHOT_FILE
    assert res and os.path.exists(ss_file)
    # clean up
    for f in glob.glob(cfg.TEST_TMP_DIR + '/*.jpg'):
        os.unlink(f)
    