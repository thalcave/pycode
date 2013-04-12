import os
import errno
import stat
import sys

def isdir(path):
    return os.path.isdir(path) and not os.path.islink(path)

def remove_file(path):
    os.remove(path)

def remove_dir(path):
    os.rmdir(path)


def rmtree(path, delete_root=True):
    print path
    names = []
    try:
        names = os.listdir(path)
    except os.error:
        pass
    cwd = os.getcwd()
    try:
        os.chdir(path)
        print "chdir: ", path
        for name in names:
            if isdir(name):
                rmtree(name)
            else:
                remove_file(name)
        os.chdir(cwd)
    except OSError, oerr:
        print "OS error({0}), {1}: {2}".format(oerr.errno, oerr.strerror, oerr.filename)
        os.chdir(cwd)
        raise
    except:
        print "Unexpected error:", sys.exc_info()[0]
        os.chdir(cwd)
        raise

    if delete_root:
        if isdir(path):
            remove_dir(path)
        else:
            remove_file(path)


def rmtree2(path, delete_root=True):
    names = []
    try:
        os.chdir(path)
        print "chdir: ", path
        names = os.listdir(".")
    except os.error:
        pass
    for name in names:
        #fullname = os.path.join(path, name)
        if isdir(name):
            rmtree2(name)
        else:
            remove_file(name)
            print "remove_file: ", name
    os.chdir("..")
    print "chdired: ", path
    if delete_root:
        if isdir(path):
            remove_dir(path)
        else:
            remove_file(path)


#rmtree2("./ln")
os.system("rm -fr ln/*")