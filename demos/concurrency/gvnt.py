#!/usr/bin/env python

"""
not a good idea
"""

from jabbapylib.math.euler import is_prime
from gevent.pool import Pool

UPTO = 10
cnt = 0

def process(n):
    global cnt
    if is_prime(n):
        cnt += 1

def main():
    num_worker_threads = UPTO
    pool = Pool(num_worker_threads)
    for n in xrange(1, UPTO):
        pool.apply_async(process, args=(n,))
    pool.join()
    print cnt

#############################################################################

if __name__ == "__main__":
    main()