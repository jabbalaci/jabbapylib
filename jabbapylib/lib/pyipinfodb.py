#!/usr/bin/env python

# https://github.com/sonicrules1234/pyipinfodb
 
# Copyright (c) 2010, Westly Ward
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the pyipinfodb nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY Westly Ward ''AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL Westly Ward BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import json, urllib, urllib2, socket
class IPInfo() :
    def __init__(self, apikey) :
        self.apikey = apikey
    def GetIPInfo(self, baseurl, ip=None, timezone=False) :
        """Same as GetCity and GetCountry, but a baseurl is required.  This is for if you want to use a different server that uses the the php scripts on ipinfodb.com."""
        passdict = {"output":"json", "key":self.apikey}
        if ip :
            try :
                passdict["ip"] = socket.gethostbyaddr(ip)[2][0]
            except : passdict["ip"] = ip
        if timezone :
            passdict["timezone"] = "true"
        else :
            passdict["timezone"] = "false"
        urldata = urllib.urlencode(passdict)
        url = baseurl + "?" + urldata
        urlobj = urllib2.urlopen(url)
        data = urlobj.read()
        urlobj.close()
        datadict = json.loads(data)
        return datadict

    def GetCity(self, ip=None, timezone=False) :
        """Gets the location with the context of the city of the given IP.  If no IP is given, then the location of the client is given.  The timezone option defaults to False, to spare the server some queries."""
        baseurl = "http://api.ipinfodb.com/v2/ip_query.php"
        return self.GetIPInfo(baseurl, ip, timezone)

    def GetCountry(self, ip=None, timezone=False) :
        """Gets the location with the context of the country of the given IP.  If no IP is given, then the location of the client is given.  The timezone option defaults to False, to spare the server some queries."""
        baseurl = "http://api.ipinfodb.com/v2/ip_query_country.php"
        return self.GetIPInfo(baseurl, ip, timezone)

