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

TEST_ASSETS_DIR = os.path.dirname(__file__) + '/../tests/_assets'
TEST_TMP_DIR = os.path.dirname(__file__) + '/../tests/_tmp'

if __name__ == "__main__":
    print TEST_ASSETS_DIR