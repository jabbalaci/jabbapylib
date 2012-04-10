#!/usr/bin/env python

"""
Working with the Gnome desktop environment.

Some operations are achieved differently under
Gnome 2 and Gnome 3. 

This is a dispatcher, you should use this 
module because it will call the appropriate 
implementation of the operation, depending 
on the version of your Gnome session.

# from jabbapylib.platform.gnome import gnome
"""

import sys
from jabbapylib.process import process

def get_gnome_session_version():
    version = process.get_simple_cmd_output('gnome-session --version')
    return int(version.split()[1][0])    # main version number
ver = get_gnome_session_version()

if ver == 2:
    import gnome2 as g
elif ver == 3:
    import gnome3 as g
else:
    raise Exception('Warning! Your Gnome version is not (yet) supported. Send us a bug report.')

#############################################################################

def set_wallpaper(img):
    """Set a given image as desktop wallpaper.
    
    img must be given in absolute path.""" 
    g.set_wallpaper(img)
    
def get_wallpaper():
    """Get the path of the currently set wallpaper."""
    return g.get_wallpaper()

#############################################################################
    
if __name__ == "__main__":
    print 'Gnome main version:', get_gnome_session_version()
    print get_wallpaper()
