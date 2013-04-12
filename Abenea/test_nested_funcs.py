#!/usr/bin/env python

def f1(x):
    def f2():
        print x
    return f2

action = f1(1)
action()

f1(2)()
f1(3)()
