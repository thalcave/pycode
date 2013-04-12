#!/usr/bin/env python

def incrementer(step=1):
    """returns a function which increments its value"""
    x = 0
    #v = dict(x=0)
    def inner():
        x += 1
        return x
        #return v['x']
    return inner

if __name__ == '__main__':
    f = incrementer()

    for x in range (1,10):
        print "f: ",f()
