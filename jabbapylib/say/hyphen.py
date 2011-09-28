#!/usr/bin/env python

"""
Hyphenate words.
Plus: pronounce them too.

Tested with Linux only.

Usage:
======
./hyphen.py <word>

Example:
========
./hyphen.py python

Output:
-------
Word:          python
Hyphenation:   py-thon
Pronunciation: http://sp.dictionary.com/dictstatic/dictionary/audio/luna/P09/P0975800.mp3

If you have mplayer installed, the mp3 is played.
"""

import re
import sys
from urllib import unquote

from jabbapylib.web import web
from jabbapylib.web.scraper import lx
from jabbapylib.audio import audio

_template = 'http://dictionary.reference.com/browse/{word}' 


def get_hyphen(doc):
    """Extract the hyphenation of a word.
    
    Replace the Unicode dot too.""" 
    try:
        hyphen = doc.cssselect('div.header h2.me')[0].text
        hyphen = hyphen.replace(u'\xb7', '-')
    except IndexError:
        hyphen = None
        
    return hyphen


def get_mp3(doc):
    """Extract the first mp3 file and return its URL.
    
    Return None if nothing is found."""
    mp3 = None
    for script in doc.cssselect('script[type="text/javascript"]'):
        if script.text is not None and 'soundUrl' in script.text:
            result = re.search('soundUrl=(http.*?mp3)', script.text)
            if result:
                mp3 = result.group(1)
                break
    
    return unquote(mp3) if mp3 else None


def process(word):
    """Process the given word.
    
    The return value is a tuple: (word, hyphenation, pronunciation mp3)."""
    url = _template.format(word=word)
    html = web.get_page(url, user_agent=True)
    doc = lx.to_doc(html)
    
    return (word, get_hyphen(doc), get_mp3(doc))


def print_result(word, hyphen, mp3):
    """Print the result and play the audio file."""
    print "Word:          {word}".format(word=word)
    if hyphen:
        print "Hyphenation:   {hyphen}".format(hyphen=hyphen)
    if mp3:
        print "Pronunciation: {mp3}".format(mp3=mp3)
        #audio.play(mp3, background=True)
        audio.play(mp3)
        

#############################################################################


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for index,arg in enumerate(sys.argv[1:]):
            if index > 0:
                print '=' * 5
            (word, hyphen, mp3) = process(arg)
            print_result(word, hyphen, mp3)
    else:
        print >>sys.stderr, "{0}: error: specify one or more words.".format(sys.argv[0])
        sys.exit(1)
