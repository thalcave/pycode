#!/usr/bin/env python

"""
Simple decorators
"""

import time
import logging
logging.basicConfig(level = logging.DEBUG)
from functools import wraps

def logging_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print "function: {0} called with args: {1}".format(func.__name__, [x for x in args])
        start_time = time.time()
        ret = func(*args)

        logging.debug('calling %s: %ss' % (func.__name__,  time.time()-start_time))
        return ret
    return wrapper

@logging_decorator
def fun_first(a):
    """dummy function"""
    print "fun_first: {0}".format(a)

@logging_decorator
def fun_second(a, b):
    """dummy function"""
    print "fun_second: {0}, {1}".format(a, b)
    time.sleep(b)


if __name__ == '__main__':
    #fun_first(10)

    fun_first(11)
    fun_second(100, 2)

