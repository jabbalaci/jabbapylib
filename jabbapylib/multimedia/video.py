#!/usr/bin/env python

"""
Working with video files.
* get video information
* take a screenshot from a video at a given time
"""

import re
import os
from jabbapylib.process import process
import jabbapylib.config as cfg

MPLAYER_SCREENSHOT_FILE = '00000001.jpg'

screenshot = "/usr/bin/mplayer '{0}' -ss '{1}' -noautosub -frames 1 -ao null -vo jpeg:outdir='{2}'"
video_info = "/usr/bin/mplayer '{0}' -ao null -vo null -frames 1 -identify"


def get_video_info(video_file):
    """Get info about a video.
    
    The info is returned by mplayer. The result is a 
    dictionary whose keys start with 'ID_'.
    """
    cmd = video_info.format(video_file)
    output = process.get_simple_cmd_output(cmd)
    return dict(re.findall('(ID_.*)=(.*)', output))


def get_video_length(video_file):
    """Get the length of a video in seconds.
    
    The length is extracted with mplayer.
    The return value is a real number.
    """
    info = get_video_info(video_file)
    return float(info['ID_LENGTH'])


def get_video_summary(video_file):
    """Get a one-line summary of the video file.
    
    Example: 'VIDEO:  [WMV3]  320x240  24bpp  1000.000 fps  386.0 kbps (47.1 kbyte/s)'
    """
    cmd = video_info.format(video_file)
    output = process.get_simple_cmd_output(cmd)
    return re.findall("VIDEO\:.*", output)[0]

def make_screenshot(video_file, sec, outdir='/tmp', rm=True):
    """Make a screenshot from a video at a given time.
    
    Work is done with mplayer. Specify the video file,
    the time in seconds when to take the screenshot,
    and the output directory. If rm is True, a previous
    screenshot file is removed first.
    By default, the screenshot is named 00000001.jpg.
    """
    # by default, mplayer saves here the screenshot: 
    full_path = os.path.join(outdir, MPLAYER_SCREENSHOT_FILE)
    if rm and os.path.exists(full_path):
        os.remove(full_path)
    
    cmd = screenshot.format(video_file, sec, outdir)
    #print cmd
    if process.get_return_code_of_simple_cmd(cmd) == 0:
        if os.path.exists(full_path):
            return full_path
    # else
    return None

#############################################################################

if __name__ == "__main__":
    video = cfg.TEST_ASSETS_DIR + '/video.avi'
    print get_video_info(video)
    print make_screenshot(video, 4)
    print get_video_length(video)
    print get_video_summary(video)
    