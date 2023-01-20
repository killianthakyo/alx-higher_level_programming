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
        for new_line in range(self.__y):
            print("")
        for i in range(self.__height):
            for space in range(self.__x):
                print(" ", end='')
            for j in range(self.__width):
                print("{}".format("#"), end="")
            print("")

    def __str__(self):
        '''Override the __str__ method to return desired format'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the rectangle instance with args
        Arguments:
            *args:
                arg1 (int): 1st argument which is id
                arg2 (int): 2nd arg which is width
                arg3 (int): 3rd arg which is height
                arg4 (int): 4th arg which is x
                arg5 (int): 5th arg which is y
        """
        if (args) and (len(args) != 0):
            count = 0
            for arg in args:
                if count == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif count == 1:
                    self.width = arg
                elif count == 2:
                    self.height = arg
                elif count == 3:
                    self.x = arg
                elif count == 4:
                    self.y = arg
                count += 1
        elif (kwargs) and (len(kwargs) != 0):
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
