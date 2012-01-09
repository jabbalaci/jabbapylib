#!/usr/bin/env python

import os
import jabbapylib.config as cfg


def test_check():
    """Check if required files exist. If something is missing, try
    to install it, otherwise some functionalities of the library
    won't work."""
    for f in cfg.required_files:
        assert os.path.isfile(f)
