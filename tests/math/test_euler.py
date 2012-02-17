from jabbapylib.math import euler

def test_is_prime():
    for p in [2,3,5,7,11,13,17,19,23]:
        assert euler.is_prime(p)
    for np in [4,6,8,9,10,12,14,15,16,18,20,21,22]:
        assert not euler.is_prime(np)
        
def test_divisors():
    assert euler.divisors(15) == [1, 3, 5, 15]
    assert euler.divisors(21) == [1, 3, 7, 21]
    assert euler.divisors(28) == [1, 2, 4, 7, 14, 28]
    
def test_number_of_divisors():
    assert len(euler.divisors(15)) == euler.number_of_divisors(15)
    assert len(euler.divisors(21)) == euler.number_of_divisors(21)
    assert len(euler.divisors(28)) == euler.number_of_divisors(28)
    assert len(euler.divisors(2012)) == euler.number_of_divisors(2012)
    
def test_prime_generator():
    assert euler.prime_generator(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, \
           29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert len(euler.prime_generator(100000)) == 9592