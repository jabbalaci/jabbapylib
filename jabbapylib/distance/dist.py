#!/usr/bin/env python

"""
various distances

# from jabbapylib.distance import lev_dist
# from jabbapylib.distance import ham_dist
# from jabbapylib.distance import similarity
"""

def lev_dist(s,t):
    """
    The Levenshtein distance (or edit distance) between two strings 
    is the minimal number of "edit operations" required to change 
    one string into the other. The two strings can have different 
    lengths. There are three kinds of "edit operations": deletion, 
    insertion, or alteration of a character in either string.

    Example: the Levenshtein distance of "ag-tcc" and "cgctca" is 3.
    source: http://en.wikibooks.org/wiki/Algorithm_implementation/Strings/Levenshtein_distance#Python
    """
    s = ' ' + s
    t = ' ' + t
    d = {}
    S = len(s)
    T = len(t)
    for i in range(S):
        d[i, 0] = i
    for j in range (T):
        d[0, j] = j
    for j in range(1,T):
        for i in range(1,S):
            if s[i] == t[j]:
                d[i, j] = d[i-1, j-1]
            else:
                d[i, j] = min(d[i-1, j] + 1, d[i, j-1] + 1, d[i-1, j-1] + 1)
    return d[S-1, T-1]


def ham_dist(s1, s2):
    """
    The Hamming distance is defined between two strings of equal length. 
    It measures the number of positions with mismatching characters.
    """
    assert len(s1) == len(s2)
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))


def similarity(s1, s2):
    """
    If you need the number of matching character positions.
    """
    assert len(s1) == len(s2)
    return sum(ch1 == ch2 for ch1, ch2 in zip(s1, s2))

############################################################################

if __name__ == "__main__":
    a = 'ag-tcc'
    b = 'cgctca'
    print lev_dist(a, b)   # 3
    #
    a = 'toned'
    b = 'roses'
    print ham_dist(a, b)   # 3
    #
    a = 'toned'
    b = 'roses'
    print similarity(a, b)    # 2
    