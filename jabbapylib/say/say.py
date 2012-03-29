#!/usr/bin/env python

"""
Text to speech.
https://pythonadventures.wordpress.com/2011/09/02/linux-python-text-to-speech/

say: say arbitrary text (low quality)

say_with_google: say just one word (high quality)

# from jabbapylib.say.say import say_with_google
"""

import os
from jabbapylib.web import web
from jabbapylib.filesystem import fs
from jabbapylib.multimedia.play import play
from jabbapylib import config as cfg

template = 'https://ssl.gstatic.com/dictionary/static/sounds/de/0/{word}.mp3'


def say(text):
    """Say a given text.
    
    It calls espeak."""
    cmd = '{espeak} "{text}" 2>/dev/null'.format(espeak=cfg.ESPEAK, text=text)
    os.system(cmd)
    

def say_with_google(word, autoremove=True, background=False, debug=False):
    """
    Say a word with Google.
    
    https://ubuntuincident.wordpress.com/2012/03/27/audio-pronunciation-of-words-from-google/
    The return value is a tuple: (found, mp3_file), where 
    found is True if the word was retrieved successfully (False otherwise), and
    mp3_file is the path of the locally saved mp3 (or None if it was not saved).
    Set autoremove to False if you want to work with the mp3 later, when this
    function returned.
    The function stores the mp3 files in /tmp.
    """
    found = False       # Was the mp3 successfully found?
    mp3_file = None     # Is the locally saved mp3 file kept?
    url = template.format(word=word)
    content = web.get_page(url, user_agent=True)
    if content:
        found = True
        fname = '/tmp/{word}.mp3'.format(word=word)
        fs.store_content_in_file(content, fname, overwrite=True)
        mp3_file = fname
        if not debug:
            play(fname, background=background)
        if autoremove:
            os.unlink(fname)
            mp3_file = None
    else:
        found = False
        mp3_file = None
    
    return (found, mp3_file)

#############################################################################
    
if __name__ == "__main__":
    text = "linux text to speech"
    say(text)
    print say_with_google('python')
