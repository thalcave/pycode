#!/usr/bin/env python

error_dict = {
    1: "my err",
    2: "second error"
}

def bkctrl_error(code):
    """map an error code to actual error"""
    print error_dict[code]


bkctrl_error(1)
bkctrl_error(2)
bkctrl_error(3)



