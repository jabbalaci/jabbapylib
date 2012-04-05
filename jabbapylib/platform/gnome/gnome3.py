#!/usr/bin/env python

"""
Working with Gnome 3. Don't use this module directly.

You should use the module "gnome".
"""

import shlex
from subprocess import call, PIPE
from jabbapylib.process import process


def set_wallpaper(img):
    """Set the given file as wallpaper."""
    
    uri = 'file://' + img
    cmd = 'gsettings set org.gnome.desktop.background picture-uri {uri}'.format(uri=uri)
    call(shlex.split(cmd), stdout=PIPE)
    
def get_wallpaper():
    """Get the path of the file that is set as wallpaper."""
    
    cmd = 'gsettings get org.gnome.desktop.background picture-uri'
    uri = process.get_simple_cmd_output(cmd)
    return uri.replace("'", "")

#############################################################################
    
if __name__ == "__main__":
    print get_wallpaper()
