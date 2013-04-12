#!/usr/bin/env python

import sys
import os
import subprocess
from subprocess import call
import fnmatch
import fileinput

def find_replace_2(fname):
    # conversions
    dict_conv = {'int' : "strToInt", 'unsigned\ int': "strToUnsignedInt", 'unsigned' : "strToUnsignedInt", 
                 'long' : "strToLong", 'unsigned\ long' : "strToUnsignedLong", 'bool' : "strToBool" }

    for i, line in enumerate(fileinput.input(fname, inplace = 1)):
        for k,v in dict_conv.iteritems():
            search = "boost::lexical_cast<" + k + ">"
            sys.stdout.write(line.replace(search, v))


def find_replace(fname):

    if "conversionFunctions" in fname:
        return

    # conversions
    dict_conv = {'int' : "strToInt", 'unsigned int': "strToUnsignedInt", 'unsigned' : "strToUnsignedInt", 
                 'long' : "strToLong", 'unsigned long' : "strToUnsignedLong", 'bool' : "strToBool" }

    with open(fname, 'r+') as mfile:
        content = mfile.read()
        for k,v in dict_conv.iteritems():
            search = "boost::lexical_cast<" + k + ">"
#            print search
            content = str.replace(content, search, v)
        mfile.seek(0)
        mfile.truncate(0)
        mfile.write(content)

#            if 'schedlogEvent(logconn' in line:
#                if 'event::BKS_COMMAND_LINE' in line:
#                    items = line.split(',')
                    # get current event
#                    citem = items[5].strip()
#                    print "logCmdLine({0}, optmap[\"::cachedir\"]->asString(), optmap.cmdLine());".format(citem)
#                else:
#                    print line,
#            else:
#                print line,

def get_file_list():
    rootPath = '.'
    pattern = '*.cpp'
 
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern):
            cfile = os.path.join(root, filename)
            find_replace(cfile)


def replace_file_list(key, value):
    """search for key in all files; return matching files"""
    search = "boost::lexical_cast<" + key + ">"
    print search



if __name__ == '__main__':

    # conversions
    dict_conv = {'int' : "strToInt", 'unsigned int': "strToUnsignedInt", 'unsigned' : "strToUnsignedInt", 
                 'long' : "strToLong", 'unsigned long' : "strToUnsignedLong", 'bool' : "strToBool" }

    get_file_list()

#    for k,v in dict_conv.iteritems():
        #print "{0} -- > {1} ".format(k,v)
#        file_list = get_file_list()
        #print "file list: {0} ".format(file_list)

