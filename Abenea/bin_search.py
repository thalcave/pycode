#!/usr/bin/env python

def bin_search_slice(l, x):
    """implement binary search in l for x, using slice"""
    if not l:
        return None

    #we asume that the list is sorted
    k = (len(l)-1)/2

    if l[k] == x:
        return k

    if l[k] < x:
        val = bin_search_slice(l[k+1:],x)
        if val is None:
            return None
        else:
            return val+k+1
    else:
        return bin_search_slice(l[:k],x)

    

def bsearch(l, x):
    """implement binary search in l for x"""

    # return  if list is empty
    if not l:
        print "Empty list received"
        return None

    # sort the list
    l.sort()

    start = 0
    end = len(l)-1


    while True:
        k = (start + end)/2
       # print "k: ",k

        if l[k] == x:
            return k

        if l[k] < x:
            start = k+1
        else:
            end = k-1
        
        if (start > end):
            return None


def test_bsearch():

    print "test first..."
    assert bsearch([], 0) is None
    print "first passed"

    assert bsearch([0], 0) == 0
    print "second passed"
    

    assert bsearch([0], 1) is None
    print "third passed"
    for i in range(11):
        assert bsearch(range(11), i) == i

def test_bsearch_slice():

    print "test first..."
    assert bin_search_slice([], 0) is None
    print "first passed"

    assert bin_search_slice([0], 0) == 0
    print "second passed"
    

    assert bin_search_slice([0], 1) is None
    print "third passed"
    for i in range(11):
        print "i=",i
        print "bsearch index: ",bin_search_slice(range(11), i)
        assert bin_search_slice(range(11), i) == i



if __name__ == '__main__':
    
    mlist = [10,5,3,1,6,9,213,32,-1, 4]

    index = bsearch(mlist, 213)
    print "index: ",index

    mlist.sort()
    print "slice index: ",bin_search_slice(mlist, 213)
    print "slice index2: ",bin_search_slice(range(11), 3)


    test_bsearch()
    test_bsearch_slice()
