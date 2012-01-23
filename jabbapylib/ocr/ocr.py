#!/usr/bin/env python

"""
OCR with the Tesseract engine from Google
this is a wrapper around pytesser (http://code.google.com/p/pytesser/)

# from jabbapylib.ocr import ocr
"""

import jabbapylib.config as cfg
from jabbapylib.lib.pytesser import pytesser

TEST_DIR = cfg.TEST_ASSETS_DIR + '/pytesser'


def image_file_to_string(fname):
    """Convert an image file to text using OCR."""
    text = pytesser.image_file_to_string(fname)
    return text.rstrip('\n')
    
#############################################################################
    
if __name__ == "__main__":
    print image_file_to_string(TEST_DIR + '/fnord.tif')
    print '=' * 20
    print image_file_to_string(TEST_DIR + '/fonts_test.png')
    print '=' * 20
    print image_file_to_string(TEST_DIR + '/phototest.tif')