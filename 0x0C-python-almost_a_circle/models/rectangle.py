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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        Base.__init__(id)

    @property
    def width(self):
        '''Get width of a rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''set the width of a rectangle'''
        self.__width = value

    @property
    def height(self):
        '''set the height of a rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set the height of a rectangle'''
        self.__height = value

    @property
    def x(self):
        '''set the x-cordinate'''
        return self.__x

    @x.setter
    def x(self, value):
        '''set the x-coordinate'''
        self.__x = value

    @property
    def y(self):
        '''get the y coordinate'''
        return self.__y

    @y.setter
    def y(self, value):
        '''set the y coordinate'''
        self.__y = value
