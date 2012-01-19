#!/usr/bin/env python

import os
import jabbapylib.config as cfg


def test_check():
    """Check if required files exist. If something is missing, try
    to install it, otherwise some functionalities of the library
    won't work."""
    for f in cfg.required_files:
        assert os.path.isfile(f)
        
        
def test_tmp_dir():
    """There must be a HOME/tmp dir. Temporary cookies file is saved here."""
    d = "{home}/tmp".format(home=os.path.expanduser('~'))
    assert os.path.isdir(d)
    assert os.access(d, os.W_OK) # W_OK is for writing, R_OK for reading, etc.
