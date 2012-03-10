#!/usr/bin/env python

"""
Play a sound when the Internet connection is back.
"""

import socket
from time import sleep
from jabbapylib.network import network
from jabbapylib.multimedia.play import play
from jabbapylib.platform import platform

TIMEOUT = 3
# put a symbolic link on an audio file in your HOME directory called ~/net_alive.mp3
AUDIO = platform.get_home_dir() + '/net_alive.mp3'


def main():
    cnt = 0
    while True:
        cnt += 1
        print '# testing...' if cnt == 1 else '# test again...'
        if network.is_internet_on(method=2):
            print '# Whoa, your net is alive!'
            play(AUDIO)
            break
        else:
            print '# no connection, waiting...'
            sleep(10)

#############################################################################

if __name__ == "__main__":
    socket.setdefaulttimeout(TIMEOUT)
    main()
