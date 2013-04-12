#!/usr/bin/env python

from os.path import join
from functools import partial

def create_file(dirname, filename):    # creates a file
    """creates a regular file in the specified dir"""
    print "touch ", join(dirname, filename)

class Data:
    """Data class"""
    def __init__(self, funct, arg1, arg2):
	print "init"
        #partial(funct, arg1, arg2)()
        func1 = globals()["create_file"]
        self.f1 = partial(func1, arg1, arg2)
        #methodToCall = getattr(test_class, funct)
    def call_stage(self):
        self.f1()

class Data2:
    def __init__(self, lstage0):
	func1 = globals()[lstage0[0]]

	#mylist = list(tstage0[1:])

	self.f1 = partial(func1, *lstage0[1:])
	
        #for idx in range (1, len(tstage0)):
        #    print tstage0[idx]
    def call_stage(self):
        self.f1()


print locals()["create_file"]
dict_stage0 = { 'create_file': ["dir1/"] }
dict_stage0['create_file'].append("file.txt")
x = Data("create_file", "dir1/", "file.txt")
x.f1()


funclist = ["create_file", "dir1/", "file.txt"]
xx = Data2(funclist)
xx.call_stage()