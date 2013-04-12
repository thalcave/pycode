from os.path import join
import os
import stat
import time

def random_file(path, size):
    bufsize = 4096
    with open(path, 'wb') as f:
        for i in range(size/bufsize):
            f.write(os.urandom(bufsize))
        f.write(os.urandom(size % bufsize))


# define functions for creating, deleting, modifying etc. a file, a hlink etc.

# functions that are common for regular files, symlinks etc.
def del_file(dirname, filename):
    """removes a file from the specified dir"""
    remove_file(join(dirname, filename))

def rename_file(dirname, filename, new_fname):
    """renames dirname/filename into dirname/new_fname"""
    os.rename(join(dirname, filename), join(dirname, new_fname))

def mod_perm(dirname, filename):
    """modifies the permissions of a file"""
    os.lchmod(join(dirname, filename), 0777)

def mod_times(dirname, filename):
    """modifies the mtime and ctime of a file"""
    os.utime(join(dirname, filename), None)

# specific functions

#dir
def add_dir(dirname):
    """adds a new dir"""
    os.mkdir(dirname)


#file
def add_regfile(dirname, filename):
    """creates a file in dirname"""
    random_file(join(dirname, filename), size=1)

def mod_regfile(dirname, filename):
    """adds something in a file"""
    with open(join(dirname, filename), 'wb') as f:
        f.write(os.urandom(5))

#device
def add_char_device(dirname, filename):
    """adds a char device"""
    os.mknod(join(dirname, filename), stat.S_IFCHR, os.makedev(1, 10))

def add_block_device(dirname, filename):
    """adds a block device"""
    os.mknod(join(dirname, filename), stat.S_IFBLK, os.makedev(1, 10))

#named pipe
def add_fifo(dirname, filename):
    """adds a fifo"""
    os.mkfifo(join(dirname, filename))

#symlink
def add_symlink_good(dir1, target, sym):
    """creates a link to an existing target"""
    path1=local_path(dir1)
    if not os.path.exists(join(path1, target)):
        raise Exception("file doesn't exist:", join(path1, target))

    os.symlink(join(path1, target), join(path1, sym))

def add_dummy_symlink(dir1, target, sym):
    """creates a link to a non-existing target"""
    path1=local_path(dir1)
    if os.path.exists(join(path1, target)):
        raise Exception("file exists:", join(path1, target))

    os.symlink(join(path1, target), join(path1, sym))

def add_self_symlink(dir1, target):
    """creates a link to self"""
    path1=local_path(dir1)
    os.symlink(join(path1, target), join(path1, target))

#hardlink
def add_hardlink(dirname, target, hlink):
    """creates a hardlink"""
    os.link(join(dirname, target), join(dirname, hlink))


class Data():
    def __init__(self, name, lstage0, lstage1):
        self.func_stage_0 = globals()[lstage0[0]]
        self.args0 = lstage0[1:]

        self.func_stage_1 = globals()[lstage1[0]]
        self.args1 = lstage1[1:]

    def stage0(self):
        self.func_stage_0(*self.args0)

    def stage1(self):
        self.func_stage_1(*self.args1)

class DataString():
    def __init__(self, name, lstage0, lstage1):
        
	list_stage0=lstage0.split(';')
	#print list_stage0

        stage0_list = []
	
	for funct in list_stage0:
	    print funct
	    
	    cstring = funct.split(' ')
	    
	    print cstring
	    print cstring[0]
	    current_fct = globals()[cstring[0]]
	    current_list = [current_fct]
	    
	    for arg in cstring[1:]:
	    	current_list.append(arg)
	    print current_list
	    
	    stage0_list.append(current_list)
	
	print "stage0: ",stage0_list
	
        self.func_stage_0 = globals()[lstage0[0]]
        self.args0 = lstage0[1:]

        self.func_stage_1 = globals()[lstage1[0]]
        self.args1 = lstage1[1:]

    def stage0(self):
        self.func_stage_0(*self.args0)

    def stage1(self):
        self.func_stage_1(*self.args1)


if __name__ == "__main__":
    #add_hardlink("test", "a", "b")
    #time.sleep(1)
    #x = Data("data1", ['add_regfile', 'test', 'f1.txt'], ['add_regfile', 'test', 'f2.txt'])
    #x.stage0()
    #x.stage1()
    
    xx = DataString("data2", [ ["add_dir", "dir1"], ["add_regfile", "test/dir1", "fstage0"]], "add_regfile fstage1")
    #x.stage0()
    #x.stage1()

