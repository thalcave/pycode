#!/usr/bin/env python

# do some fs operations

from functools import partial
import call_functions
import define_functions

call_functions.perform(define_functions.action1)

test_str = "123"
call_functions.perform(partial(define_functions.action2, test_str))

file_name = "f.txt"
command = "create"
#perform(partial(action3, command, file_name))
partial(define_functions.action3, command, file_name)()

