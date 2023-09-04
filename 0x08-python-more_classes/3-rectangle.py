#!/usr/bin/python3

"""creating the class"""


class Rectangle:
    """declare the class of Rectangle"""

    def __init__(self, width=0, height=0):
        """intializing the new rectangle.
        Arg:
            width(int):the new rectangle width.
            height(int): the new rectangle height.
        Raise:
            TypeError: width and height must be an integer.
            ValueError: width and height must be  >= 0.
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
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self) -> str:
        if self.__width == 0 or self.height == 0:
            return ""
        rect = ""
        for column in range(self.__height):
            for rows in range(self.__width):
                rect += '#'
            if column < self.__height - 1:
                rect += '\n'
        return rect
