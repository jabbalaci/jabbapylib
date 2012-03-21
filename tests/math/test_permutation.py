from jabbapylib.math import permutation as perm

def test_lexicographically_next_permutation():
    cnt = 0
    li = ['a', 'b', 'c']
    cnt += 1
    while perm.lexicographically_next_permutation(li):
        cnt += 1
    assert cnt == 6
    #
    cnt = 0
    li = [3,6,6,7]
    cnt += 1
    while perm.lexicographically_next_permutation(li):
        cnt += 1
    assert cnt == 12
    #
    li = [1,2,9,6,5]
    perm.lexicographically_next_permutation(li)
    assert li == [1,5,2,6,9]
    perm.lexicographically_next_permutation(li)
    assert li == [1,5,2,9,6]
    perm.lexicographically_next_permutation(li)
    assert li == [1,5,6,2,9]
    #
    li = ['C','A','D','B']
    perm.lexicographically_next_permutation(li)
    assert li == ['C','B','A','D']
