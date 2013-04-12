#!/usr/bin/env python

import math

def isprime(n):
    """returns True if n is prime, False otherwise"""

    # 1 is not a prime number
    if n<=1:
        return False

    sqr_root =int(math.sqrt(n))+1
    #print "sqr_root: ",sqr_root

    for i in range(2, sqr_root):
        if n % i == 0:
            return False

    return True

def test_primes():
    assert not isprime(1)
    assert isprime(2)
    assert isprime(3)
    assert not isprime(4)
    assert isprime(97)

def primesuntil(n):
    """returns the prime numbers smaller than n"""

    # hold results in this list
    primes = []

    for x in range(2,n):
        if isprime(x):
            primes.append(x)

    return primes


if __name__ == '__main__':
    test_primes()

    # 1st 
    print "primes until 10: ",primesuntil(10)

    # 2nd
    # filter returns items for which function was true
    # returns a sequence consisting of those items from the sequence for which "isprime" is true
    print "primes until 100: ",filter(isprime, range(2, 100))

    # list comprehensions
    print "primes until 100: ",[x for x in range (2,100) if isprime(x)]

    # map calls function for each item and returns a list of the return values
    print "test: ",map(lambda x: x*x, filter(lambda x: x % 2 == 0, range(10)))
