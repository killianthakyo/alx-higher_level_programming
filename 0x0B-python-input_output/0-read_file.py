#!/usr/bin/python3

"""Read a file"""


def read_file(filename=""):
    """
    Read a text (UTF8) AND print it in stdout
    """
    with open(filename, mode="r", encoding="utf-8") as myFile:
        print(myFile.read(), end="")
