#!/usr/bin/env python

"""
Configuration part.
"""

import os

# portability tip: in ~/.mozilla/firefox put a symbolic link on 
# ~/.mozilla/firefox/XXXXXXXX.default/cookies.sqlite
COOKIE_DB = "{home}/.mozilla/firefox/cookies.sqlite".format(home=os.path.expanduser('~'))
ESPEAK = '/usr/bin/espeak'
MPLAYER = '/usr/bin/mplayer'
WGET = '/usr/bin/wget'
XSEL = '/usr/bin/xsel'
TIDY = '/usr/bin/tidy'    

required_files = (
    COOKIE_DB,      # to get webpages that are protected with cookies
    ESPEAK,         # text to speech
    MPLAYER,        # play audio/video
    WGET,           # get webpages
    XSEL,           # copy to clipboard
    TIDY,           # tidy up HTML source
)
