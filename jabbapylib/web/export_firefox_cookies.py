#!/usr/bin/env python

"""
This script extracts cookies from Firefox's cookies.sqlite file
that are specific to a given host. The exported cookies are saved
in the file cookies.txt.
"""

try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO
 
import sqlite3 as db
from jabbapylib import config

import cookielib


COOKIE_DB =  config.COOKIE_DB
CONTENTS = "host, path, isSecure, expiry, name, value"


def get_cookies_in_text(host):
    """Export cookies in plain-text (like cookies.txt) format. 
    
    Return value: exported cookies as a string."""
    conn = db.connect(COOKIE_DB)
    cursor = conn.cursor()
         
    sql = "SELECT {c} FROM moz_cookies WHERE host LIKE '%{h}%'".format(c=CONTENTS, h=host)
    cursor.execute(sql)
     
    out = StringIO()
    for row in cursor.fetchall():
        s = "{0}\tTRUE\t{1}\t{2}\t{3}\t{4}\t{5}".format(row[0], row[1],
                 str(bool(row[2])).upper(), row[3], str(row[4]), str(row[5]))
        print >>out, s
         
    value = out.getvalue() 
    out.close()
    conn.close()
    
    return value


def get_cookies_in_cookiejar(host):
    """Export cookies and put them in a cookiejar.
    
    Return value: a cookiejar filled with cookies."""
    # based on http://www.guyrutenberg.com/2010/11/27/building-cookiejar-out-of-firefoxs-cookies-sqlite/
    cj = cookielib.LWPCookieJar()       # This is a subclass of FileCookieJar that has useful load and save methods
    
    conn = db.connect(COOKIE_DB)
    cursor = conn.cursor()
    sql = "SELECT {c} FROM moz_cookies WHERE host LIKE '%{h}%'".format(c=CONTENTS, h=host)
    cursor.execute(sql)
    
    for item in cursor.fetchall():
        c = cookielib.Cookie(0, item[4], item[5],
            None, False,
            item[0], item[0].startswith('.'), item[0].startswith('.'),
            item[1], False,
            item[2],
            item[3], item[3]=="",
            None, None, {})
        #print c
        cj.set_cookie(c)

    return cj

    
if __name__ == "__main__":
    host = 'projecteuler'
    
    # version 1
    print get_cookies_in_text(host)

    # version 2
    cj = get_cookies_in_cookiejar(host)
    for index, cookie in enumerate(cj):
        print index, ':', cookie
    #cj.save(COOKIEFILE)    # Save the cookies in a file. Format: LWP-Cookies-2.0.