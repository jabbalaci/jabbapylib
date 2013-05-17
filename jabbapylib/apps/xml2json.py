#!/usr/bin/env python

"""
XML to JSON converter.
"""

import sys
import xmltodict
import json


def convert(xml_file, xml_attribs=True):
    with open(xml_file) as f:
        d = xmltodict.parse(f, xml_attribs=xml_attribs)
        print json.dumps(d, indent=4)

#############################################################################

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print 'Usage: {0} input.xml'.format(sys.argv[0])
        sys.exit(1)
    # else
    convert(sys.argv[1])