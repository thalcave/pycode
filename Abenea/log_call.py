#!/usr/bin/env python 

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


def df():
    """dummy function"""
    print "dummy function"

if __name__ == '__main__':
    aa = log_call(a)
    aa('blue', 1)

    ls = [1,2,3]
    bb = log_call(b)
    bb(ls)

    cc = log_call(c)
    cc('test', 4, arg3=51)



