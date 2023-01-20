#!/usr/bin/python3
'''
Rectangle class that inherits frome base class
'''
from models.base import Base


class Rectangle (Base):
    '''
    Rectangle class
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Rectangle class constructor'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Get width of a rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''set the width of a rectangle'''
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''set the height of a rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set the height of a rectangle'''
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''set the x-cordinate'''
        return self.__x

    @x.setter
    def x(self, value):
        '''set the x-coordinate'''
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''get the y coordinate'''
        return self.__y

    @y.setter
    def y(self, value):
        '''set the y coordinate'''
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''Public method that returns the area value of a rectangle'''
        return self.__width * self.__height

    def display(self):
        '''Print in stdout the Rectangle instance with the character #'''
        for i in range(self.__height):
            for j in range(self.__width):
                print("{}".format("#"), end="")
            print("")
