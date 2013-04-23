#!/usr/bin/env python


import sys
import stat
import os
import time
import logging
import imp
import hashlib
import socket

def md5(filepah):
    with open(filepah, 'rb') as f:
        m = hashlib.md5()
        while True:
            data = f.read(65536)
            if len(data) == 0:
                return m.hexdigest()
            else:
                m.update(data)


def create_big_path(target):
    """creates a big FS Tree"""
    cwd = os.getcwd()

    try:
        os.chdir(target)
        for cindex in range(0, 1000):
            current_dir = "a" + str(cindex)
            os.mkdir(current_dir)
            open("f"+str(cindex), 'wb')
            os.chdir(current_dir)
    except IOError as (errno, strerror):
        print "I/O error({0}): {1}".format(errno, strerror)
    except OSError, e:
        print "OS error({0}), {1}: {2}".format(e.errno, e.strerror, e.filename)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise
    os.chdir(cwd)

def summary(root_path, full_path):
    relative_path = full_path
    st = os.lstat(full_path)
    ret = '%s mode=%s type=%s' % (
        relative_path,
        oct(stat.S_IFMT(st.st_mode))[1:],
        stat.S_IMODE(st.st_mode))
    if not stat.S_ISLNK(st.st_mode):
        ret += 'mtime=' + str(int(st.st_mtime))
    if not stat.S_ISDIR(st.st_mode):
        ret += 'size=' + str(st.st_size)
    if os.path.isfile(full_path):
        ret += ' md5=' + md5(full_path)
  # TODO: add acls?
    return ret


def generate_summary(full_path, summary_file):
    root_path = os.path.dirname(full_path)
    to_summarize = os.path.basename(full_path)
    if len(root_path) == 0:
        root_path = full_path
        to_summarize = "."

    # if path ends with /
    if len(to_summarize) == 0:
        root_path = os.path.dirname(os.path.dirname(full_path))
        to_summarize = os.path.basename(os.path.dirname(full_path))

    if len(root_path) == 0:
        raise Exception("invalid path: "+full_path)

    print to_summarize
    print root_path
    os.chdir(full_path)

    list = []
    for d in os.walk("."):
        list.extend([os.path.join(d[0], f) for f in d[1]])
        list.extend([os.path.join(d[0], f) for f in d[2]])
    list = sorted(list)
    with open(summary_file, 'w') as f:
        for path in list:
            #print path
            if len(path) > 4090:
                print "skip path len=", len(path)
            else:
                print >>f, summary(full_path, path)


create_big_path("./ln")
#generate_summary("/mnt/download/Work/MyWork/Python/BigStruct/test", "summary")
#generate_summary("/root/frankenstein/tmp/tmpKl57Ne", "d")
#print os.path.dirname("/mnt/download/Work/MyWork/Python/BigStruct/ln/")
#print os.path.basename("/mnt/download/Work/MyWork/Python/BigStruct/ln/")
