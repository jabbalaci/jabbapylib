#!/usr/bin/env python

"""
# from jabbapylib.web.useragents import get_useragents
# from jabbapylib.web.useragents import get_random_useragent
"""

import os
import zipfile
import json
import random

PATH = os.path.dirname(os.path.abspath(__file__))


def get_useragents():
    zf = zipfile.ZipFile(PATH + '/useragents.zip', 'r')
    return json.loads(zf.read('useragents.json'))


def get_random_useragent():
    zf = zipfile.ZipFile(PATH + '/useragents.zip', 'r')
    li = json.loads(zf.read('useragents.json'))
    return random.choice(li)

#############################################################################

if __name__ == "__main__":
#    print get_random_useragent()
    print len(get_useragents())