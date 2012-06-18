#!/usr/bin/env python

"""
Simple API for geoPlugin's JSON Web Service 
(http://www.geoplugin.com/webservices/json).

Goal: having an IP, look up its country, i.e. where the given
host is located.

# from jabbapylib.network import geoinfo
"""

import re
import json
from jabbapylib.web.web import get_page

gp_template = 'http://www.geoplugin.net/json.gp?ip={ip}'


class Host(object):
    def __init__(self, ip=""):
        """
        ip is the IP of the host you want to look up.
        If no ip is provided, it will look up your own host.
        """
        self.ip = ip
        self.d = self.get_json(self.ip)
#        print self.d    # for debugging
        
    def __getitem__(self, k):
        """
        Example below. You can use these keys:
        {
          "geoplugin_request":"xxx.xxx.xxx.xxx",
          "geoplugin_status":200,
          "geoplugin_city":"Castroville",
          "geoplugin_region":"TX",
          "geoplugin_areaCode":210,
          "geoplugin_dmaCode":641,
          "geoplugin_countryCode":"US",
          "geoplugin_countryName":"United States",
          "geoplugin_continentCode":"NA",
          "geoplugin_latitude":29.360000610352,
          "geoplugin_longitude":-98.892097473145,
          "geoplugin_regionCode":"TX",
          "geoplugin_regionName":"Texas",
          "geoplugin_currencyCode":"USD",
          "geoplugin_currencySymbol":"&#36;",
          "geoplugin_currencyConverter":1
        }
        """
        return self.d[k]
    
    def get_country_code(self):
        """
        Country code of the host.
        """
        return self.d['geoplugin_countryCode']
        
    def get_json(self, ip):
        text = get_page(gp_template.format(ip=ip))
        text = re.sub('^geoPlugin\(', '', text)
        text = re.sub('\)$', '', text)
        return json.loads(text)

def main(ip):
    host = Host(ip)
    print host.get_country_code()

#############################################################################
    
if __name__ == "__main__":
    ip = '173.194.35.177'    # Google
    main(ip)