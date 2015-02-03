#!/usr/bin/env python

import os, fnmatch
import sys
import re

"""
Search and replace strings in certain files
* walk recursively a file system tree, skipping excluded dirs
* filter files based on defined extensions (*.xml, *.cpp, *.java etc.), skipping excluded files as well
* for each matching file, search for corresponding string and replace it with specific dummy string

cpp files:  QnStrings::$oldstr(.*) --> QnString::$newstr()  //can be on multiple lines

java files: Strings.$oldstr(.*) --> Strings.$newstr()       //can be on multiple lines
            R.string.$oldstr --> R.string.$newstr

xml files:  string/$oldstr -->string/$newstr

Input:
* file containing strings to be replaced (one on each line)
* path to the directory containing files to be changed

Output:
* files are modified in-place

"""

def file_is_excluded(filename, exclude_files):
    for exclusion in exclude_files:
        if filename.startswith(exclusion):
            return True
    return False

def search_replace_follow_parens(filename, replacements):
    """Search for a string in form $string(.*);
     - keep track of opened parens, go until the first one is closed and replace the whole string between ( and )
     """

    # read file content
    with open(filename) as f:
        content = f.read()

    # if file needs to be written
    dirty = False

    # search every string in content
    for current_item in replacements:
        oldstr = current_item[0]
        newstr = current_item[1]

        """replaces oldstr with newstr in line, replacing also string in parens (if exists)
        eg:
        for oldstr = 'tellAllFriendsContactsSelected', newstr = 'dummyString'
        line:
        a. 'contactsSelectedTextView.setText(Strings.tellAllFriendsContactsSelected(String.valueOf(selectedCount)))'
        b. 'contactsSelectedTextView.setText(Strings.tellAllFriendsContactsSelected());'

        result will be 'contactsSelectedTextView.setText(Strings.dummyString());'
        """

        start = 0
        while True:
            found = content.find(oldstr, start)
            if found == -1:
                break

            #number of opened parens
            opened = 1
            offset = found + len(oldstr) + 1

            if content[offset-1] != '(':
                start += 1
                continue

            while offset < len(content):
                if content[offset] != ')':
                    if content[offset] == '(':
                        opened += 1
                    offset += 1
                else:
                    offset += 1
                    opened -= 1
                    if not opened:
                        break

            content = content[:found] + newstr + "()" + content[offset:]
            print "found in '{0}' string '{1}' and replaced it with '{2}'".format(os.path.basename(filename), oldstr, newstr)
            dirty = True

            start += len(newstr)
            if start > len(content):
                break

    # if dirty, write the file
    if dirty:
        with open(filename, "w") as f:
            f.write(content)


def search_replace_exact_match(filename, replacements):
    """Use regex to replace exact matches"""

    # read file content
    with open(filename) as f:
        content = f.read()

    # if file needs to be written
    dirty = False

    # search every string in content
    for current_item in replacements:
        find = current_item[0]
        replace = current_item[1]

        # replaces all occurrences, exact match
        (content, no_subs) = re.subn(find + '\\b', replace, content)
        if no_subs:
            print "found in file '{0}' string '{1}' and replaced it with '{2}'".format(os.path.basename(filename), find, replace)
            dirty = True

    # if dirty, write the file
    if dirty:
        with open(filename, "w") as f:
            f.write(content)

def walk_tree(directory, replacements, excluded_files, excluded_dirs):
    """Walk a fs tree, skip excluded files/dirs, filter files based on extensions and apply replace functions"""

    searched_extensions = replacements.keys()
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        # skip excluded dirs
        for excl_dir in excluded_dirs:
            if excl_dir in dirs:
                dirs.remove(excl_dir)
                print "Skipping dir: {0}".format(excl_dir)

        for filename in files:
            # skip excluded files
            if file_is_excluded(filename, excluded_files):
                continue

            # process only files that have certain extensions
            for extension in searched_extensions:
                if filename.endswith(extension):
                    filepath = os.path.join(path, filename)
                    replacement_function = replacements[extension][0]
                    # apply replacement function
                    replacement_function(filepath, replacements[extension][1])
                    break

def start_replace(replacement_strings, dirname):
    cpp_replacements = list()
    java_replacements = list()
    xml_replacements = list()

    for oldstr, newstr in replacement_strings.iteritems():
        # tuple for C++ files
        cpp_string = ("QnStrings::" + oldstr, "QnStrings::" + newstr)
        cpp_replacements.append(cpp_string)

        # tuple for Java files
        java_string = ("Strings." + oldstr, "Strings." + newstr)
        java_replacements.append(java_string)

        #tuples for XML files
        xml_string1 = ('string/' + oldstr, 'string/' + newstr)
        xml_string2 = ('id/' + oldstr, 'id/' + newstr)
        xml_replacements.append(xml_string1)
        xml_replacements.append(xml_string2)

    replacements = dict()
    for ext in [".cpp", ".mm", ".cc", ".c", ".hpp", ".h"]:
        replacements[ext] = (search_replace_follow_parens, cpp_replacements)
    replacements[".java"] = (search_replace_follow_parens, java_replacements)
    replacements[".xml"] = (search_replace_exact_match, xml_replacements)

    excluded_files = ["moc", "Strings.java"]
    excluded_dirs = [".git", "Build"]

    walk_tree(dirname, replacements, excluded_files, excluded_dirs)

    #do it again for some 'special' Java files
    java_replacements = list()
    for oldstr, newstr in replacement_strings.iteritems():
        # tuple for Java files
        java_string1 = ("R.id." + oldstr, "R.id." + newstr)
        java_string2 = ("R.string." + oldstr, "R.string." + newstr)
        java_replacements.append(java_string1)
        java_replacements.append(java_string2)

    replacements.clear()
    replacements[".java"] = (search_replace_exact_match, java_replacements)

    walk_tree(dirname, replacements, excluded_files, excluded_dirs)

def read_file(filename):
    replace_strings = dict()
    with open(filename) as f:
        for line in f:
            replace_strings[str.strip(line)] = "dummyString"
    return replace_strings

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Usage: ./search_and_replace.py <filename_with_strings_to_replace> <sourcedir>"
        sys.exit(1)

    start_replace(read_file(sys.argv[1]), sys.argv[2])
