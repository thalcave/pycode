#!/usr/bin/env python

import os

def create_big_path(target):
    """creates a big structure"""
    for cdir in ["a", "b", "c", "d", "e", "f", "g", "h", "k", "l", "m", "n", "o", "p", "q"]:
        current_dir = ""
        for cindex in range(0, 500):
            current_dir = current_dir + cdir + str(cindex) + "/"
            os.makedirs(current_dir)
            open(current_dir + "file.txt", 'wb')
            #print current_dir
            #print current_dir + "file.txt"

create_big_path(".")