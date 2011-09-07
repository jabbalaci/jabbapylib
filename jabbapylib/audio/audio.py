#!/usr/bin/env python

"""
Playing audio files.
"""

import os

def play(audio_file, background=False):
    """Play an audio file with mplayer."""
    cmd = '/usr/bin/mplayer {audio} 1>/dev/null 2>&1'.format(audio=audio_file)
    if background:
        cmd += ' &'
    os.system(cmd)

#############################################################################
    
if __name__ == "__main__":
    audio = '/home/jabba/dwhelper/Santigold_-_Unstoppable.mp3'
    play(audio, background=True)