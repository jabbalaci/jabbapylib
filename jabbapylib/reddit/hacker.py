#!/usr/bin/python

"""
Based on http://beza1e1.tuxen.de/articles/titles.html .

Returns a random hacker title, suitable for business cards :)

# from jabbapylib.hacker import hacker
"""

from random import choice
from jabbapylib.filesystem import fs
from jabbapylib import config as cfg

INPUT = cfg.ROOT_DIR + '/reddit/hacker.json'


def get_random_title():
    """Returns a random hacker title."""
    d = fs.read_json(INPUT)
    li = d['for_business_cards']
    return choice(li)

#############################################################################

if __name__ == "__main__":
    print get_random_title()