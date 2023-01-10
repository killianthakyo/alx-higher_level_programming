#!/usr/bin/python3
"""
Write to a file
"""


def write_file(filename="", text=""):
    """
    Writing to a file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)
