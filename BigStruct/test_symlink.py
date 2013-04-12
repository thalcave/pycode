import os
import stat

def touch_file(fname):
    """touch a file"""
    
    #first, check if it's a symlink
    file_status = os.lstat(fname)
    if stat.S_ISLNK(file_status.st_mode):
        print "file is link: ", fname
        target = os.readlink(fname)
        # re-create symlink (in order to change the times of it)
        # first, remove symlink
        
        os.symlink(target, fname)
    else:
        print "file is not link: ", fname
        os.utime(fname, None)


touch_file("f1.txt")
touch_file("sl")
