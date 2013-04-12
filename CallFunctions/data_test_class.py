#!/usr/bin/env python

from os.path import join
from functools import partial
import os
import stat

def create_file(dirname, filename):    # creates a file
    """creates a regular file in the specified dir"""
    print "touch ", join(dirname, filename)

def remove_file(dirname, filename):    # removes a file
    """removes a file from specified dir"""
    print "rm ", join(dirname, filename)
    
def mod_perm(dirname, filename):
    """modifies the permissions of a file"""
    os.chmod(join(dirname, filename), 0777)
    
def mod_times(dirname, filename):
    """modifies the atime, mtime and ctime of a file"""
    open(join(dirname, filename), 'w').close()

def mod_regfile(dirname, filename):
    """modifies a file in dirname"""
    with open(join(dirname, filename), 'wb') as f:
        f.write(os.urandom(5))

#device
def add_char_device(dirname, filename):
    """adds a char device"""
    os.mknod(join(dirname, filename), stat.S_IFCHR, os.makedev(1, 10))

def add_block_device(dirname, filename):
    """adds a block device"""
    os.mknod(join(dirname, filename), stat.S_IFBLK, os.makedev(1, 10))

def rename_file(dirname, filename, new_fname):
    """renames dirname/filename into dirname/new_fname"""
    os.rename(join(dirname, filename), join(dirname, new_fname))


class Data:
    def __init__(self, lstage0, lstage1):
        func0 = globals()[lstage0[0]]
        self.func_stage_0 = partial(func0, *lstage0[1:])

        func1 = globals()[lstage1[0]]
        self.func_stage_1 = partial(func1, *lstage1[1:])
	
    def call_stage0(self):
        self.func_stage_0()
    def call_stage1(self):
        self.func_stage_1()


fstage0 = ["create_file", "dir1/", "file.txt"]
fstage1 = ["remove_file", "dir1/", "file.txt"]
xx = Data(fstage0, fstage1)
xx.call_stage0()
xx.call_stage1()


#mod_perm(".","test.txt")
mod_times(".","test.txt")

mod_regfile(".","test.txt")

add_block_device(".","testblockdev")
add_char_device(".","testchardev")

mod_perm(".","testblockdev")


rename_file(".","testblockdev", "testbldev")
