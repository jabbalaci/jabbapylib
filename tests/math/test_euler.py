import pytest
from jabbapylib import config as cfg
from jabbapylib.filesystem import fs
from jabbapylib.math import euler

def test_is_prime():
    assert not euler.is_prime(1)
    for p in [2,3,5,7,11,13,17,19,23]:
        assert euler.is_prime(p)
    for np in [4,6,8,9,10,12,14,15,16,18,20,21,22]:
        assert not euler.is_prime(np)
        
def test_is_prime_mr():
    a_under_1000 = [i for i in range(2, 1000) if euler.is_prime(i)]
    b_under_1000 = [i for i in range(2, 1000) if euler.is_prime_mr(i)]
    assert a_under_1000 == b_under_1000
        
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
    
def test_get_primes_between():
    li = [2, 3, 5, 7, 11, 13, 17, 19]
    assert euler.get_primes_between(1, 23) == li
    #
    with pytest.raises(AssertionError):
        euler.get_primes_between(-1, 23)
    #
    with pytest.raises(AssertionError):
        euler.get_primes_between(4294967290, 4294967296)
    
def test_gen_primes():
    """See if it generates correctly the primes below 1000."""
    etalon = fs.read_json(cfg.TEST_ASSETS_DIR + '/primes_below_1000.json')
    #
    li = []
    primes = euler.gen_primes()
    for p in primes:
        if p > 1000:
            break
        li.append(p)
    #
    assert li == etalon

def test_prime_divisors():
    assert euler.prime_divisors(504) == [2, 2, 2, 3, 3, 7]
    
def test_is_palindrome():
    assert not euler.is_palindrome('jabba')
    assert euler.is_palindrome('radar')

def test_inc_avg():
    li = [2,6,4,7,3]
    avg1 = sum(li) / float(len(li))
    assert avg1 == euler.inc_avg(li)
    #
    li = [10,8,2,4,15,12,21,7]
    li = li[2:-2]   # take a slice of the list
    avg1 = sum(li) / float(len(li))
    assert avg1 == euler.inc_avg(li)
    
def test_eulers_totient_phi():
    assert int(euler.eulers_totient_phi(36)) == 12
    assert int(euler.eulers_totient_phi(12)) == 4