#!/bin/sh

# these are required for jabbapylib

sudo apt-get install \
    curl \
    gtk2-engines-pixbuf \
    libxml2-dev \
    libxslt-dev \
    lynx \
    lynx-cur \
    mplayer2 \
    python-imaging \
    python-lxml \
    python-qt4 \
    python-sympy \
    python2.7-dev \
    python-xlib \
    sqlite3 \
    tidy \
    xsel \
    bsdgames \
    fping \
    libmpfr-dev \
    libgmp3-dev

# tesseract-ocr was removed
# you'd better install it from source
# the one in the Ubuntu repo. is very old
