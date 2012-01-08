#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Work with unicode texts.
"""

import unicodedata

#def unicode_to_ascii(text):
#    try:
#        text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')
#    except TypeError:
#        pass
#    
#    return text

def remove_accents(input_str):
    # http://stackoverflow.com/questions/517923
    nkfd_form = unicodedata.normalize('NFKD', unicode(input_str, 'utf8'))
    return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])


def remove_non_ascii(text): 
    return ''.join(c for c in text if ord(c) < 128)

#############################################################################
    
if __name__ == "__main__":
    text = "László"
    print remove_accents(text)
    print remove_non_ascii(text)