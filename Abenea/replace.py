#!/usr/bin/env python

import sys

def replace(fname):
    with open(fname, 'r') as mfile:
        for line in mfile:
            if 'schedlogEvent(logconn' in line:
                if 'event::BKS_COMMAND_LINE' in line:
                    items = line.split(',')
                    # get current event
                    citem = items[5].strip()
                    print "logCmdLine({0}, optmap[\"::cachedir\"]->asString(), optmap.cmdLine());".format(citem)
                else:
                    print line,
            else:
                print line,


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "usage : ./replace <filename>"
        sys.exit(1)

    replace(sys.argv[1])
