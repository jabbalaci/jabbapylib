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


COOKIE_DB =  config.COOKIE_DB
CONTENTS = "host, path, isSecure, expiry, name, value"


def get_cookies(host):
    """Export cookies. Return value: exported cookies as a string."""
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

    
if __name__ == "__main__":
    host = 'projecteuler'
    print get_cookies(host)
