#!/usr/bin/env python

"""
Working with Gnome 2. Don't use this module directly.

You should use the module "gnome".
"""

import shlex
from subprocess import call, PIPE
from jabbapylib.process import process


def set_wallpaper(img, mode='stretched'):
    """Set the given file as wallpaper.
    
    Possible modes: wallpaper, centered, scaled, stretched."""
    cmd1 = "gconftool-2 --type=string --set /desktop/gnome/background/picture_options {mode}".format(mode=mode)
    cmd2 = "gconftool-2 --type=string --set /desktop/gnome/background/picture_filename {img}".format(img=img)
    
    call(shlex.split(cmd1), stdout=PIPE)
    call(shlex.split(cmd2), stdout=PIPE)

    
def get_wallpaper():
    """Get the path of the file that is set as wallpaper."""
    
    cmd = "gconftool-2 --get /desktop/gnome/background/picture_filename"
    return process.get_simple_cmd_output(cmd)

#############################################################################
    
if __name__ == "__main__":
    print get_wallpaper()
