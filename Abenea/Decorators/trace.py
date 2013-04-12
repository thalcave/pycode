#!/usr/bin/env python

"""
Decorators used for tracing
"""

from functools import wraps

def trace(afunc):
    """Trace entry, exit and exceptions.

    afunc is the function to be decorated
    """
    def logged_func(*args, **kw):
        """Trace this function."""
        print "enter", afunc.__name__
        try:
            result = afunc( *args, **kw )
        except Exception, e:
            print "exception", afunc.__name__, e
            raise
        print "exit", afunc.__name__
        return result
    logged_func.__name__= afunc.__name__
    logged_func.__doc__= afunc.__doc__
    return logged_func

def trace2(afunc):
    """Trace entry, exit and exceptions.

    afunc is the function to be decorated
    """
    @wraps(afunc)#Without the use of this decorator factory, the name of the example function would have been 'wrapper',
    def logged_func(*args, **kw):
        """Trace this function."""
        print "enter", afunc.__name__
        try:
            result = afunc( *args, **kw )
        except Exception, e:
            print "exception", afunc.__name__, e
            raise
        print "exit", afunc.__name__
        return result
    return logged_func

def msquare(a):
    """returns square(a)"""
    return a*a

# this line enables the use of this file as standalone program
if __name__ == '__main__':
    f = trace(msquare)
    print f(999)
    print f.__name__


    f2 = trace2(msquare)
    print f2.__name__

    print f2.__name__
