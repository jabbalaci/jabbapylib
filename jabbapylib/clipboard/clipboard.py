#!/usr/bin/env python

"""
Copy text to clipboards (to both of them).
"""

import subprocess


def text_to_clipboards(text):
    # "primary":
    xsel_proc = subprocess.Popen(['xsel', '-pi'], stdin=subprocess.PIPE)
    xsel_proc.communicate(text)
    # "clipboard":
    xsel_proc = subprocess.Popen(['xsel', '-bi'], stdin=subprocess.PIPE)
    xsel_proc.communicate(text)

#############################################################################
    
if __name__ == "__main__":
    text = "this should go on the clipboards"
    text_to_clipboards(text)