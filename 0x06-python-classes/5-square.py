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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if not isinstance(self.size, int):
            raise TypeError("size must be an integer")
        if self.size < 0:
            raise ValueError("size must be >= 0")
        """Print hash"""
        x = 0
        while x < self.size:
            y = 0
            while y < self.size:
                print("#", end="")
                y = y + 1
            print("")
            x = x + 1
        if self.size == 0:
            print("")
