#!/usr/bin/env python

"""
Download the background image of the day from BING
and set it as your Gnome desktop wallpaper.

Tested under Ubuntu GNU/Linux. This script requires 
the 'jabbapylib' library, available via PyPI.

Inspired by http://spsneo.com/blog/2009/07/18/set-bing-background-as-your-desktop-wallpaper-in-gnome/ ,
where the author provides a PHP solution.

Usage:
======
(1) Customize the SAVE_DIR variable below. Images will be stored there.
(2) Call this script once a day. The best way is to put it in the crontab.

# from jabbapylib.apps import bing
"""

import os
from jabbapylib.web import web #@UnresolvedImport
from urlparse import urljoin
from jabbapylib.dateandtime.dateandtime import get_date_from_year_to_day
from jabbapylib.platform.gnome import gnome
from jabbapylib.dateandtime.dateandtime import get_unix_date
from urllib import unquote

URL = 'http://www.bing.com'
SAVE_DIR = '/trash/bing'


def extract(test=False):
    text = web.get_page(URL)
    text = text.split('g_img={url:')[1]
    text = text.split(',')[0].replace("'", "")
    img_url = urljoin(URL, text)
    fname = img_url.split('/')[-1]
    fname = unquote(fname).split('/')[-1]
    if not test:
        print '# fname:', fname
    save_name = '{date}-{fname}'.format(date=get_date_from_year_to_day(), fname=fname) 
    return (img_url, save_name)

def download(url, fname):
    dest = "{dir}/{fname}".format(dir=SAVE_DIR, fname=fname)
    cmd = "wget '{url}' -O {dest}".format(url=url, dest=dest)
    
    if os.path.isfile(dest):
        os.unlink(dest)
    os.system(cmd)
    return dest

def main():
    print '# --------------------'
    img_url, save_name = extract()
    print '#', get_unix_date()
    print '#', img_url
    saved = download(img_url, save_name)
    print '# saved to', saved
    gnome.set_wallpaper(saved)

#############################################################################

if __name__ == "__main__":
    main()