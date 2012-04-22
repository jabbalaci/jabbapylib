#!/usr/bin/env python

"""
Get a wallpaper from the net and set it as your Gnome wallpaper.
Two functionalities:
(1) Call it with a URL => download and set
(2) Call it with a local file => set
"""

import os
import sys
from urllib import unquote
from jabbapylib.filesystem import fs
from jabbapylib.platform.gnome import gnome
from jabbapylib.dateandtime.dateandtime import get_date_from_year_to_day

SAVE_DIR = '/trash/wallpaper'


def download(url):
    fname = url.split('/')[-1]
    save_name = '{date}-{fname}'.format(date=get_date_from_year_to_day(), fname=fname)
    #
    dest = "{dir}/{sname}".format(dir=SAVE_DIR, sname=save_name)
    cmd = "wget '{url}' -O {dest}".format(url=url, dest=dest)
    
    if os.path.isfile(dest):
        os.unlink(dest)
    os.system(cmd)
    print '# saved to', dest
    return dest


def check(path):
    if not fs.is_image_file(path):
        print >>sys.stderr, "Error: provide an _image_ file."
        sys.exit(1)
    #
    if fs.is_local_path(path) and not os.path.isfile(path):
        print >>sys.stderr, "Error: the input file doesn't exist."
        sys.exit(1)
        

def main(args):
    param = args[0]
    check(param)
    
    if fs.is_local_path(param):
        fname = os.path.abspath(param)
    else:
        fname = download(param)
        
    gnome.set_wallpaper(fname)

#############################################################################

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print >>sys.stderr, "Error: provide a parameter (URL or path of an image file)."
        sys.exit(1)
    else:
        main(sys.argv[1:])