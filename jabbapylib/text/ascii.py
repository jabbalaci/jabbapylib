#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Work with unicode texts.
"""

import unicodedata


def unicode_to_ascii(text):
    try:
        text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')
    except TypeError:
        pass
    
    return text


def remove_non_ascii(text): 
    return ''.join(c for c in text if ord(c) < 128)



#############################################################################
    
if __name__ == "__main__":
    text = "Kellemes Ünnepeket!"
    print unicode_to_ascii(text)