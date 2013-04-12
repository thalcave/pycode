#!/usr/bin/env python 

from functools import wraps

import time


import logging
logging.basicConfig(level=logging.DEBUG)


def a(color, size=5):
    #print "Function a color: {0} size: {1}".format(color, size)
    pass

def b(l):
    #print "Function B: ",l
    pass

def c(arg1, arg2, arg3):
    #print "Function C"
    pass


def log_call(f):
    def inner(*args, **kwargs):
        tmp = [repr(k) for k in args]
        tmp.extend(["%s=%s" % (str(k), repr(v)) for k,v in kwargs.iteritems()])
        logging.debug('calling %s(%s)' % (f.__name__, ",".join(tmp)))
        return f(*args, **kwargs)
    return inner

def time_call(f):
    """decorator function"""
    @wraps(f)
    def inner(*args, **kwargs):
        start = time.clock()

        tmp = [repr(k) for k in args]
        tmp.extend(["%s=%s" % (str(k), repr(v)) for k,v in kwargs.iteritems()])

        ret = f(*args, **kwargs)
        logging.debug('calling %s(%s): %ss' % (f.__name__, ",".join(tmp), time.clock()-start))
        
        return ret
    return inner

# The @ syntax calls the decorator with the function from the following line 
@log_call
def test(*args):
    print "Test"

@time_call
def f():
    pass

@time_call
def square(n):
    return len([(x, y) for x in range(n) for y in range(n)])


def logging_decorator(f):
    # wrapper.__name__ = f.__name__
    @wraps(f)
    def wrapper(*args, **kwargs):
        print "before"
        ret  = f()
        print "after"
        return ret
    return wrapper

@logging_decorator
def hi():
    print "hi"


def df():
    """dummy function"""
    print "dummy function"

if __name__ == '__main__':
    a = log_call(a)
    a('blue', 1)

    ls = [1,2,3]
    b = log_call(b)
    b(ls)

    c = log_call(c)
    c('test', 4, arg3=51)

    test(1,2,3)
    test(range(1,10))


    hi()
    print hi.__name__

    print "-----------------------"

    print f()
    print square(700)
    print square.__name__


    f()
