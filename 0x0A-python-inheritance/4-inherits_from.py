#!/usr/bin/python3
"""check direct inheritance"""


def inherits_from(obj, a_class):
    """check if if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    Arguments:
        obj (any): obj to check
        a_class (type): class to be checked against
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
