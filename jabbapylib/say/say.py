#!/usr/bin/env python

"""
Text to speech.
https://pythonadventures.wordpress.com/2011/09/02/linux-python-text-to-speech/
"""

import os
import jabbapylib.config as cfg

def say(text):
    """Say a given text.
    
    It calls espeak."""
    cmd = '{espeak} "{text}" 2>/dev/null'.format(espeak=cfg.ESPEAK, text=text)
    os.system(cmd)

#############################################################################
    
if __name__ == "__main__":
    text = "linux text to speech"
    say(text) 