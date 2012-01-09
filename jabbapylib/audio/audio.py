#!/usr/bin/env python

"""
Playing audio files.
"""

import os
import jabbapylib.config as cfg

def play(audio_file, background=False):
    """Play an audio file with mplayer."""
    cmd = '{mplayer} {audio} 1>/dev/null 2>&1'.format(mplayer=cfg.MPLAYER, audio=audio_file)
    if background:
        cmd += ' &'
    os.system(cmd)

#############################################################################
    
if __name__ == "__main__":
    audio = cfg.ASSETS_DIR + '/audio.mp3'
    play(audio, background=True)