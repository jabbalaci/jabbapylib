#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
algorithms that are useful for Project Euler (http://projecteuler.net)

# from jabbapylib.math import euler
# from jabbapylib.math.euler import is_palindrome
# from jabbapylib.math.euler import is_prime
# from jabbapylib.math.euler import get_primes_between
"""

import random
from jabbapylib import config as cfg
from subprocess import Popen, PIPE

# used in is_prime_mr()
_mrpt_num_trials = 5    # number of bases to test


def is_prime(n):
    """
    Decide whether a number is prime or not.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    maxi = n**0.5 + 1
    while i <= maxi:
        if n % i == 0:
            return False
        i += 2

    return True

 
def is_prime_mr(n):
    """
    Miller-Rabin primality test.
 
    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    
    Source: http://rosettacode.org/wiki/Miller-Rabin_primality_test#Python
    """
    if n < 2:
        return False
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)
 
    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
 
    for _ in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
 
    return True # no base tested showed n as composite


def divisors(n):
    """
    Divisors of n.
    
    Example: divisors of 28: 1,2,4,7,14,28.
    """
    li = [1]

    half = n/2
    for i in range(2, half+1):
        if n % i == 0:
            li.append(i)
            
    # this way the list remains sorted
    if n > 1:
        li.append(n)

    return li


def number_of_divisors(n):
    """
    Number of divisors of n.
    """
    cnt = 1
    if n > 1:
        cnt += 1
    half = n/2
    for i in range(2, half+1):
        if n % i == 0:
            cnt += 1

    return cnt


def prime_generator(maxi):
    """
    Generate all the prime numbers below maxi. maxi is not included.
    
    The method uses Aristotle's sieve algorithm.
    """
    li = []
    for _ in range(maxi):
        li.append(1)

    li[0] = li[1] = 0

    for pos,val in enumerate(li):
        if val:
            for index in range(pos+pos,maxi,pos):
                li[index] = 0

    primes = []
    for pos,val in enumerate(li):
        if val:
            primes.append(pos)

    return primes


def get_primes_between(start, stop):
    """
    Wrapper for the Unix command primes (can be found
    in the package bsdgames).
    Usage: primes start stop (where stop is not included)
    
    WARNING!!! The stop value must not be greater than 4294967295.
    If the stop value is greater, you'll get WRONG results!
    
    Alternative: make a loop from start to stop and test each number
    with the Miller-Rabin test (is_prime_mr()). Slower but more
    reliable than this one for very large numbers.
    """
    assert start >= 0 and stop <= 4294967295
    #
    li = []
    proc = Popen([cfg.PRIMES, str(start), str(stop)],stdout=PIPE)
    while True:
        line = proc.stdout.readline()
        if line:
            li.append(int(line))
        else:
            break
    #
    return li


def gen_primes():
    """
    It's a generator, so use it like any other.
    
    primes = gen_primes()
    for p in primes:
        print p
    
    Found at http://stackoverflow.com/questions/2211990 .
    """
    D = {}
    q = 2  # first integer to test for primality.
    
    while True:
        if q not in D:
            # not marked composite, must be prime  
            yield q 
            
            #first multiple of q not already marked
            D[q * q] = [q] 
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            # no longer need D[q], free memory
            del D[q]
        
        q += 1


def prime_divisors(n):
    """
    Prime divisors.
    """
    li = []

    np = gen_primes()
    while n != 1:
        prime = np.next()
        while n % prime == 0:
            n /= prime
            li.append(prime)

    return li


def is_palindrome(s):
    """
    Decide if a string is a palindrome or not.
    
    Palindrome: you get the same string reading backwards.
    """
    return s == s[::-1]


def inc_avg(li):
    """
    Calculate the average incrementally.
    Input: a list.
    Output: average of the list.
    See http://ubuntuincident.wordpress.com/2012/04/25/calculating-the-average-incrementally/ .
    """
    left = 0
    right = len(li)-1

    avg = li[left]
    left += 1

    while left <= right:
        curr = left + 1
        avg += (li[left] - avg) / float(curr)
        left += 1

    return avg


def eulers_totient_phi(num):
    """
    Euler's totient (a.k.a. phi) function, φ(n).
    
    Count the number of positive integers less than or equal 
    to "n" that are relatively prime (coprimes) to "n".
    
    Coprimes: if the only positive integer that evenly divides 
              two numbers is 1. This is the same thing as their 
              greatest common divisor is 1.
    
    https://secure.wikimedia.org/wikipedia/en/wiki/Totient_function
    """
    dpd = set(prime_divisors(num))    # distinct_prime_divisors

    phi = num
    for p in dpd:
        phi *= (1 - (1.0 / float(p)))
        
    return phi

############################################################################# 
 
if __name__ == "__main__":
    print is_palindrome('jabba')
    print is_palindrome('radar')
    
    # primes below 1 million
#    primes = gen_primes()
#    for p in primes:
#        if p > 1000000:
#            break
#        print p
        
    print prime_divisors(504)
    print prime_divisors(36)
    print eulers_totient_phi(36)
    print eulers_totient_phi(12)
    #
    print get_primes_between(1, 23)