#!/usr/bin/python3
"""
Append and return count
"""


def append_write(filename="", text=""):
    """
    Append and return number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        x = f.write(text)
    return x
