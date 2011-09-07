#!/usr/bin/env python

"""
Configuration part.
"""

import os

# portability tip: in ~/.mozilla/firefox put a symbolic link on 
# ~/.mozilla/firefox/XXXXXXXX.default/cookies.sqlite
COOKIE_DB = "{home}/.mozilla/firefox/cookies.sqlite".format(home=os.path.expanduser('~'))

required_files = (
    COOKIE_DB,              # to get webpages that are protected with cookies
    '/usr/bin/espeak',      # text to speech
    '/usr/bin/mplayer',     # play audio/video
    '/usr/bin/wget',        # get webpages
    '/usr/bin/xsel'         # copy to clipboard
)

def check():
    """Check if required files exist. If something is missing, try
    to install it, otherwise some functionalities of the library
    won't work."""
    for f in required_files:
        print f,':',
        if os.path.isfile(f):
            print '[OK]'
        else:
            print '[not found]'
            

#############################################################################
    
if __name__ == "__main__":
    check()