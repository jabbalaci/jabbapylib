#!/usr/bin/env python

"""
Generate the lexicographically next permutation of a sequence
of elements.

Pseudo-code:

1. Find the largest index k such that a[k] < a[k + 1]. 
   If no such index exists, the permutation is the last permutation.
2. Find the largest index l such that a[k] < a[l]. 
   Since k + 1 is such an index, l is well defined and satisfies k < l.
3. Swap a[k] with a[l].
4. Reverse the sequence from a[k + 1] up to and including the final element a[n].

# from jabbapylib.math import permutation as perm
"""

def lexicographically_next_permutation(a):
    """
    Generates the lexicographically next permutation.
    
    Input: a permutation, called "a". This method modifies
    "a" in place. Returns True if we could generate a next
    permutation. Returns False if it was the last permutation
    lexicographically.
    """
    i = len(a) - 2
    while not (i < 0 or a[i] < a[i+1]):
        i -= 1
    if i < 0:
        return False
    # else
    j = len(a) - 1
    while not (a[j] > a[i]):
        j -= 1
    a[i], a[j] = a[j], a[i]        # swap
    a[i+1:] = reversed(a[i+1:])    # reverse elements from position i+1 till the end of the sequence
    return True


def get_some(n):
    li = ['c', 'a', 'b', 'e', 'd']
    print li    # process
    print
    while lexicographically_next_permutation(li) and n:
        print li    # process
        n -= 1

#############################################################################

if __name__ == "__main__":
#    li = ['a', 'b', 'c']
#    print li    # process
#    while lexicographically_next_permutation(li):
#        print li    # process
    get_some(3)
