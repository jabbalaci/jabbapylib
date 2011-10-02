#!/usr/bin/env python

"""
Weather.
"""
try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO

import jabbapylib.web.web as web
import jabbapylib.text.ascii as ascii


def main(url):
    html = web.get_page(url, user_agent=True)
    txt = web.html_to_text(html, method=web.HTML2TEXT)
    
    #txt = ascii.unicode_to_ascii(txt)
    #txt = txt.replace(u'\xb7', '-')
    #txt = ascii.remove_non_ascii(txt).encode('ascii')

    
    print_result(txt)
    
    
def print_result(txt):
    f = StringIO(txt)
    for line in f:
        if 'Copyright (C) 2011 Farlex' in line:
            break
        # else
        line = line.strip()
        if line:
            print line
        
    f.close()
    


#############################################################################

if __name__ == "__main__":
    url = 'http://www.thefreedictionary.com/p/apprenticeship'
    main(url)