#!/usr/bin/python3

"""creating the class"""


class Rectangle:
    """declare the class of Rectangle"""

    def __init__(self, width=0, height=0):
        """initializing the new rectangle.
        Arg:
            width(int):the width of the new rectangle.
            height(int):the height of the new rectangle.
        Raise:
            TypeError: width and height must be integer.
            ValueError: width and height must be >= 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise  ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise  ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

