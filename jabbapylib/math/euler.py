#!/usr/bin/env python

"""
algorithms that are useful for Project Euler (http://projecteuler.net)

# from jabbapylib.math import euler
"""

def is_prime(n):
    """
    Decide whether a number is prime or not.
    """
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
