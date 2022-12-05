#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for let in my_string:
        if let != 'c' and let != 'C':
            new_str = new_str + let
    return new_str
