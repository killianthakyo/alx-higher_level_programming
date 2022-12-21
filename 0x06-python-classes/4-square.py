#!/usr/bin/python3

"""Define an empty class called Square"""


class Square:
    """Initialize the Square class"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size**2

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size
