#!/usr/bin/env python

import sys

def parseResults(fname):
    """parse a file, get avg file size"""

    no_files = 0
    no_bytes = 0
    
    # open the file
    with open(fname, 'r') as f:
        for line in f:


            if line.startswith("Files"):
                no_files = long(line.split()[2])
                no_bytes = 0

            if line.startswith("File bytes processed"):
                no_bytes = long(line.split()[3])

            if no_files and no_bytes:
                avg = (float(no_bytes)/float(no_files))

                print "no_files: {0} no_bytes: {1} avg: {2:.3f}".format(no_files, no_bytes, avg)

                no_files = 0


if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        raise RuntimeError("usage: ./get_avg_filesize.py <results>")

    fname=sys.argv[1]

    print "fname: ",fname

    parseResults(fname)


