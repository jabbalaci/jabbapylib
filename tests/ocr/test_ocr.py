from jabbapylib.ocr import ocr
import jabbapylib.config as cfg
import ocr_examples as ex

TEST_DIR = cfg.TEST_ASSETS_DIR + '/pytesser'


def test_image_file_to_string():
    print 'tesseract version:', cfg.MY_TESSERACT
    #
    res = ocr.image_file_to_string(TEST_DIR + '/fnord.tif')
    assert res == 'fnord' or res == 'fnorcl'
    #
    #res = ocr.image_file_to_string(TEST_DIR + '/fonts_test.png')
    #print res
    #
    res = ocr.image_file_to_string(TEST_DIR + '/phototest.tif')
    assert res == ex.PHOTOTEST_TIF