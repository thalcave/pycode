#!/usr/bin/env python

"""
Fibonacci implementations
"""

import itertools

def fib_recursive(nval):
    """Recursive Fibonacci"""

    if nval <= 1:
        return nval
    return fib_recursive(nval-1) + fib_recursive(nval-2)

def fib_iterative(nval):
    """Iterative Fibonacci"""
    if nval <= 1:
        return nval

    prev = 0
    cval = 1

    for idx in range(2, nval+1):
        tmp = prev + cval
        prev = cval
        cval = tmp

    return cval

class Fibonacci:
    """Infinite iterator for Fibonacci numbers"""
    def __init__(self):
        self.nval = -1
        self.prev = 0
        self.cval = 1

    def __iter__(self):
        """must return self to make the iterator iterable."""
        return self

    def next(self):
        self.nval += 1

        if self.nval <= 1:
            return self.nval

        tmp = self.prev + self.cval
        self.prev = self.cval
        self.cval = tmp

        return self.cval


def fibonacci_generator():
    """Generator for Fibonacci"""

    yield 0
    yield 1

    prev = 0
    cval = 1

    while 1:
        prev, cval = cval, prev+cval
        yield cval

def fib():
    yield 0

    a, b = 0, 1
    while 1:
        yield b
        a, b = b, a+b

def test_fib(func):
    """Test Fibonacci function"""

    values = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
    for idx, val in enumerate(values):
        ret_val = func(idx)
        #print ret_val
        assert (val == ret_val), "expected: {0} got: {1} for nval: {2}".format(val, ret_val, idx)

def test_iterator(func):
    values = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

    # Make an iterator that returns selected elements from the iterable.
    ret_val = list(itertools.islice(func(), 13))

    assert (values == ret_val), \
           "\nexp: {0}\ngot: {1}\n".format(values, ret_val)


if __name__ == '__main__':
    test_fib(fib_recursive)
    test_fib(fib_iterative)

    test_iterator(Fibonacci)
    test_iterator(fibonacci_generator)
    test_iterator(fib)
