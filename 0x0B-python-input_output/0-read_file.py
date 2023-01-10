#!/usr/bin/python3

"""Write into a file"""


def read_file(filename=""):
    with open(filename, mode="r", encoding="utf-8") as myFile:
        print(myFile.read())
