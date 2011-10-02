#!/usr/bin/env python

"""
Weather.
"""
try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO

import re
import sys

import jabbapylib.web.web as web
import jabbapylib.text.ascii as ascii

_template = 'http://www.thefreedictionary.com/p/{word}'

def process(word):
    url = _template.format(word=word)
    html = web.get_page(url, user_agent=True)
    txt = web.html_to_text(html).decode('utf-8')
    
    #txt = ascii.unicode_to_ascii(txt)
    txt = txt.replace(u'\xb7', '-')
    txt = ascii.remove_non_ascii(txt).encode('ascii')
    txt = re.sub('\[.*?.gif\]', '', txt)
    
    print_result(txt)
    
    
def print_result(txt):
    f = StringIO(txt)
    hr = 0
    for line in f:
        line = line.rstrip('\n')
        if re.search('\s+_+\s*', line):
            hr += 1
            continue
        line = re.sub('\(.*$', '', line)
        line = re.sub('^.*\)', '', line)
        if 'Copyright' in line and 'Farlex, Inc.Source URL' in line:
            break
        if 'The Free Dictionary' in line or 'thefreedictionary.com' in line:
            continue
        # else
        #if hr > 0 and hr < 3:
        #    print line
        print line
        
    f.close()
    


#############################################################################

if __name__ == "__main__":    
    if len(sys.argv) > 1:
        process(sys.argv[1])
    else:
        print >>sys.stderr, "{0}: error: specify a word.".format(sys.argv[0])
        sys.exit(1)