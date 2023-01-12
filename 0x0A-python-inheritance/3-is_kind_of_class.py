#!/usr/bin/python3
"""
check for inheritance
"""


def is_kind_of_class(obj, a_class):
    '''
    Determine if the object is an instance of of class
    '''
    if isinstance(obj, a_class):
        return True
    return False
