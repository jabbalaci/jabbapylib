#!/usr/bin/env python

"""
Playing audio (and video too) files.

# from jabbapylib.multimedia.play import play
"""

import os
import jabbapylib.config as cfg

def play(audio_file, background=False, debug=False):
    """Play an audio file with mplayer."""
    cmd = '{mplayer} {audio}'.format(mplayer=cfg.MPLAYER, audio=audio_file)
    if not debug:
        cmd += ' 1>/dev/null 2>&1'
    if background:
        cmd += ' &'
    os.system(cmd)

#############################################################################
    
if __name__ == "__main__":
    audio = cfg.TEST_ASSETS_DIR + '/audio.mp3'
    play(audio, background=True)