#!/usr/bin/env python

import types

class B0:
    pass

class B1(B0):
    pass

class B2(B0):
    pass

class D(B1,B2):
    pass

def dfs(a, visited, order):
    visited.add(a)
    for base in a.__bases__:

        if base not in visited:
            order.append(base)
            dfs(base, visited, order)

def attrsearch_order(a):

    vis = set()
    od = list()
    od.append(a)
    if type(a) == types.InstanceType:
        print "a is an instance"
        print "a dict: {0}".format(a.__class__)
        od.append(a.__class__)
        dfs(a.__class__, vis, od)
    else:
        print "Start: {0}".format(a.__name__)
        dfs(a, vis, od)

    for x in od:
        print "order : {0}".format(x)
    return od

def test_attrsearch_order():
    # the previous example
    class B0: pass
    class B1(B0): pass
    class B2: pass
    class D(B1, B2): pass
    d_inst = D()
    assert attrsearch_order(d_inst) == [d_inst, D, B1, B0, B2]

    # diamond inheritance
    class B0: pass
    class B1(B0): pass
    class B2(B0): pass
    class D(B1, B2): pass
    assert attrsearch_order(D) == [D, B1, B0, B2]


if __name__ == '__main__':

    #print "dictB0: {0}".format(B0.__dict__)
    print "dictB1: {0}".format(B1.__dict__)
    #print "dictB1 name: {0}".format(B1.__name__)
    #print "B1.baseclasses: {0}".format(B1.__bases__)

    #for k,v in B1.__dict__.iteritems():
        #print "key: {0} val: {1}".format(k,v)

    attrsearch_order(B0)
    attrsearch_order(B1)
    attrsearch_order(B2)
    #print attrsearch_order(D)

    assert attrsearch_order(D) == [D, B1, B0, B2]
    
    attrsearch_order(D())

    #print dir(D)


    test_attrsearch_order()
