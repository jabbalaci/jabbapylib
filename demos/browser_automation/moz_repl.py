#!/usr/bin/env python

import re
from time import sleep
import telnetlib

HOST = 'localhost'
PORT = 4242

prompt = [r'repl\d*> ']    # list of regular expressions

def get_page(url, wait=3):
    tn = telnetlib.Telnet(HOST, PORT)
    tn.expect(prompt)
    cmd = "content.location.href = '{url}'".format(url=url)
    tn.write(cmd + "\n")
    tn.expect(prompt)
    if wait:
        print '# waiting {X} seconds...'.format(X=wait)
        sleep(wait)
        print '# continue'
    #
    tn.write('content.document.body.innerHTML\n')
    html = tn.expect(prompt)[2].split('\n')
    if html[0].strip() == '"':
        html = html[1:]
    if re.search(prompt[0], html[-1]):
        html = html[:-1]
    if html[-1].strip() == '"':
        html = html[:-1]
    tn.write("repl.quit()\n")
    return html

##################################

if __name__ == "__main__":
    print 'OK'
    html = get_page('http://simile.mit.edu/crowbar/test.html')
    for line in html:
        print line
    print '================'
    print 'Death'
    url = 'http://www.ncbi.nlm.nih.gov/nuccore/CP002059.1'
    html = get_page(url, wait=30)
    for line in html:
        print line
