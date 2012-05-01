#!/usr/bin/env python

"""
A very simple wrapper for the Linux command "ping".
Currently, it determines the average response time of a host.

# from jabbapylib.network.ping import ping
"""

import re
from jabbapylib.process import process

def ping(url, cnt=1):
    """Ping a URL and return the average ping time."""
    cmd = 'ping -c {cnt} {url}'.format(url=url, cnt=cnt)
    output = [x for x in process.get_simple_cmd_output(cmd).split('\n') if x]
    result = re.search('min/avg/max/mdev = (.*)/(.*)/(.*)/(.*) ms', output[-1])
    if result:
        return float('{0:.2f}'.format(float(result.group(1))))
    else:
        return None

#############################################################################
    
if __name__ == "__main__":
    url = 'www.google.com'
    print ping(url)