#!/usr/bin/env python

"""
Lookup by IP.
"""

import readline
from pprint import pprint
from jabbapylib.lib import pyipinfodb
import webbrowser

API_KEY = '9a35831cf1637910474e3b736207ae1d7d5999b53177cda97320ccc34af80aac'


def main():
    info = pyipinfodb.IPInfo(apikey=API_KEY)
    ip = raw_input("IP: ")
    result = info.GetCity(ip=ip)
    pprint(result)

    inp = raw_input("Show on map (y/n) [default: yes]? ")
    if inp in ('', 'y'):
        url = "https://maps.google.com/maps?q={lat},{long}".format(lat=result['Latitude'], long=result['Longitude'])
        webbrowser.open_new_tab(url)
    
#############################################################################

if __name__ == "__main__":
    main()
