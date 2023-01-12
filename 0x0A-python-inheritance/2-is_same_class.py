#!/usr/bin/python3
"""
check for inheritance
"""


def is_same_class(obj, a_class):
    '''
    Determine if an object is exactly an instance of specified class
    '''
    if type(obj) is a_class:
        return True
    return False
