#!/usr/bin/env python

"""
algorithms that are useful for Project Euler (http://projecteuler.net)

# from jabbapylib.math import euler
# from jabbapylib.math.euler import is_palindrome
# from jabbapylib.math.euler import is_prime
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


def gen_primes():
    """It's a generator, so use it like any other.
    
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
    """Prime divisors."""
    li = []

    np = gen_primes()
    while n != 1:
        prime = np.next()
        while n % prime == 0:
            n /= prime
            li.append(prime)

    return li


def is_palindrome(s):
    """Decide if a string is a palindrome or not.
    
    Palindrome: you get the same string reading backwards."""
    return s == s[::-1]

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
