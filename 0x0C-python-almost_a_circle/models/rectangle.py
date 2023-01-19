#!/usr/bin/python3
'''
Rectangle class that inherits frome base class
'''


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
        Base.__init(id)

    @property
    def get_width(self):
        return self.__width

    @width.setter
    def set_width(self, value):
        self.__width = value

    @property
    def get_height(self):
        return self.__height

    @height.setter
    def set_height(self, value):
        self.__height = value

    @property
    def get_x(self):
        return self.__x

    @x.setter
    def set_x(self, value):
        self.__x = value

    @property
    def get_y(self):
        return self.__y

    @y.setter
    def set_y(self, value):
        self.__y = value
