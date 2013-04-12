#!/usr/bin/env python

import sys

def do_nothing(str):
    return str

def do_lower(str):
    return str.lower()


def set_case(case_sensitive):
    if case_sensitive:
        return do_nothing

    return do_lower

def word_count(fname, case_sensitive):
    # if not case sensitive

    # keep words counter
    counter = {}


    do_case = set_case(case_sensitive)

    with open(fname, 'r') as mfile:
        for line in mfile:
            # usage of split(" ") will not group together consecutive delimiters
            item_list = do_case(line).split()

            for x in item_list:
                counter[x] = 1 + counter.get(x, 0)


    print counter

    
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "usage : ./file_word_counter <filename> <case_sensitive>: 0 = no | 1 = yes"
        sys.exit(1)

    case_sensitive = bool(int(sys.argv[2]))
    #print "case sensitive {0}".format(case_sensitive)

    
    word_count(sys.argv[1], case_sensitive)
