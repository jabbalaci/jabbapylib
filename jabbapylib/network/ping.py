#!/usr/bin/env python

"""
A very simple wrapper for the Linux command "ping".
Currently, it determines the average response time of a host.

# from jabbapylib.network.ping import ping
"""

import re
from jabbapylib.process import process


def ping(host, cnt=1):
    """Ping a URL and return the average ping time."""
    cmd = 'ping -c {cnt} {url}'.format(url=host, cnt=cnt)
    output = [x for x in process.get_simple_cmd_output(cmd).split('\n') if x]
    result = re.search('min/avg/max/mdev = (.*)/(.*)/(.*)/(.*) ms', output[-1])
    if result:
        return float('{0:.2f}'.format(float(result.group(1))))
    else:
        return None


def fping(host, cnt=1):
    """
    Get the avg ping time of a host (in msec).

    Instead of ping we use the command fping.
    """
    host = host.split(':')[0]
    cmd = "fping {host} -C {cnt} -q".format(host=host, cnt=cnt)
    res = [float(x) for x in process.get_simple_cmd_output(cmd).strip().split(':')[-1].split() if x != '-']
    if len(res) > 0:
        return sum(res) / len(res)
    else:
        return None

#############################################################################
    
if __name__ == "__main__":
    host = 'www.google.com'
    print ping(host, 2)
    print fping(host, 2)