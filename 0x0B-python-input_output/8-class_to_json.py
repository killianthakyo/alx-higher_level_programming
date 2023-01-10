#!/usr/bin/python3
"""
Return the dics representation
"""


def class_to_json(obj):
    '''
        Returns the dict representation of a class
    '''
    return (getattr(obj, "__dict__"))
