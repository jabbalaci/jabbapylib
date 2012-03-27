#!/usr/bin/env python

"""
Convert image file to string.
"""

import sys
from jabbapylib.ocr.ocr import image_file_to_string

def process(files):
    """
    Process each image file and OCR them. The result 
    is printed to the stdout.
    """
    for index,f in enumerate(files):
        if index > 0:
            print '-' * 10
        print image_file_to_string(f)

#############################################################################
    
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print 'Error: provide an image file.'
        sys.exit(1)
    # else
    process(sys.argv[1:])