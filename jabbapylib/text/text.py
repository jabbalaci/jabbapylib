#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
using textblob
"""

from textblob import TextBlob

#############################################################################

if __name__ == "__main__":
    text = u"""
Amikor ismeretlenek elrabolják Thuviát, Ptarth hercegnőjét, Carthoris, a Mars urának fia az első számú gyanúsított. És csakis Carthoris mentheti meg a leányt, aki szerelmet ültetett a szívébe.
"""
    blob = TextBlob(text)
    print blob.detect_language()