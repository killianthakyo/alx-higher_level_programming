#!/usr/bin/python3
"""
add_integer:
This function adds two integers. Returns an integer
"""

def add_integer(a, b=98):
    """
    Function that returns sum of two numbers
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return int(a + b)
