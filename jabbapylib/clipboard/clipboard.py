#!/usr/bin/env python

"""
Copy text to clipboards (to both of them).

# from jabbapylib.clipboard.clipboard import text_to_clipboards
"""

import subprocess


def text_to_clipboards(text):
    """Copy text to both clipboards."""
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