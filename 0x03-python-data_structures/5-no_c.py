#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for l in my_string:
        if l != 'c' and l != 'C':
            new_str = new_str + l
    return new_str
