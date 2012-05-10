#!/usr/bin/env python

from jabbapylib.math.euler import is_prime

UPTO = 1000000
cnt = 0

def main():
    global cnt
    for n in xrange(1, UPTO):
        if is_prime(n):
            cnt += 1
    print cnt

#############################################################################

if __name__ == "__main__":
    main()