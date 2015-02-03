#!/usr/bin/env python

import os
import glob
import subprocess
import stat


def get_core_name(core_dir):
    #get last core from dir
    search_pattern=os.path.join(core_dir, 'core.*')
    latest_core=max(glob.iglob(search_pattern), key = os.path.getctime)
#    print "latest core file {0}".format(latest_core)
    return latest_core

def get_exec_name(current_dir, latest_core):
    if latest_core:
        result = subprocess.check_output(["file", latest_core])
        print result
        tmp = result.split()
        if len(tmp) > 12:
            tmp2=tmp[12]
            if tmp2[-1] == '\'':
                return tmp2[3:-1]
            return tmp2[3:]

    return ""

def find_exec(name, path):
    print path
    print name
    executable = stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH
    for root, dirs, files in os.walk(path):
#        print filename
        for fname in files:
#            print fname
            if fname == name:
#                print "FOUND"
                st = os.stat(os.path.join(root, fname))
                mode=st.st_mode
                if mode & executable:
                    return os.path.join(root, fname)
    return ""

if __name__ == '__main__':
    COREDIR="/home/florin.micu/cores"
    ROOTEXEC="/home/florin.micu/Work/Qnective/florin.micu/Build/gcc46_ubuntu12_Debug"

    lcore = get_core_name(COREDIR)
    if not lcore:
        print "No core found, will exit"
        os.exit(1)

    exec_name = get_exec_name(COREDIR, lcore)
    if exec_name:
        full_path = find_exec(exec_name, ROOTEXEC)
        print full_path
        print "latest core: {0}".format(lcore)
        if full_path:
            subprocess.call(["gdb", full_path, lcore])
