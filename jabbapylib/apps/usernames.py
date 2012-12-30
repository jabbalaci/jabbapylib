#!/usr/bin/env python

"""
Username generator.
"""

from jabbapylib.lib.markov_usernames import MName


def main():
    li = []
    for i in range(10):
        li.append(MName().New())
    for e in sorted(li):
        print e

#############################################################################

if __name__ == "__main__":
    main()
