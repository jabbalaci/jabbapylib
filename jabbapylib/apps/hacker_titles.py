#!/usr/bin/python

"""
Conversion of http://beza1e1.tuxen.de/articles/titles.html
into a Python script.
"""

from random import choice
from jabbapylib.filesystem import fs
from jabbapylib import config as cfg

INPUT = cfg.ROOT_DIR + '/reddit/hacker.json'
MAX = 5


def print_titles(li, text):
    print text
    print '-' * len(text)
    for index in xrange(MAX):
        title = choice(li)
        li.remove(title)
        print '({i}) {title}'.format(i=index+1, title=title)


def main():
    d = fs.read_json(INPUT)
    print_titles(d['for_business_cards'], 'Hacker Titles for Business Cards')
    print
    print_titles(d['not_really_for_business_cards'], 'And some more, not so suited for business cards')

#############################################################################

if __name__ == "__main__":
    main()