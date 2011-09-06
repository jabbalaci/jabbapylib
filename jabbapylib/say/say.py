#!/usr/bin/env python

"""
Text to speech.
https://pythonadventures.wordpress.com/2011/09/02/linux-python-text-to-speech/
"""

import os

def say(text):
    cmd = '/usr/bin/espeak "{0}" 2>/dev/null'.format(text)
    os.system(cmd)

#############################################################################
    
if __name__ == "__main__":
    text = "linux text to speech"
    say(text) 