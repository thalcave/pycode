#!/usr/bin/env python

import os, fnmatch
import sys

def replace(line, replace):
    found_pos = line.find(replace)
    if found_pos == -1:
        return line

    #number of opened parens
    opened = 1
    offset = found_pos + len(replace) + 1
    while offset < len(line):
        sys.stdout.write(line[offset])

        if line[offset] != ')':
            if line[offset] == '(':
                opened += 1
            offset += 1
            continue
        
        opened -= 1
        if not opened:
            break
        offset += 1
    print

    new_string = line[:found_pos + len(replace)+1] + line[offset:]
    print new_string
    new_string = new_string.replace(replace + "()", "dummyString()")

    return new_string

if __name__ == '__main__':
    bigstring='contactsSelectedTextView.setText(Strings.tellAllFriendsContactsSelected(String.valueOf(selectedCount)));'
    smallstring='contactsSelectedTextView.setText(Strings.tellAllFriendsContactsSelected());'

    search='tellAllFriendsContactsSelected'

    print replace(bigstring, search)
    print replace(smallstring, search)
