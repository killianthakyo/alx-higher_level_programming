#!/usr/bin/python3
"""
check for inheritance
"""


def is_same_class(obj, a_class):
    '''
    Determine if an object is exactly an instance of specified class

    Arguments:
    obj (any): object to check
    a_class (type): class to be checked against
    '''
    if type(obj) is a_class:
        return True
    return False
