#!/usr/bin/python3

"""declare the inhrits the Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """intitialazing the square"""

    def __init__(self, size):
        """initialazing the new square"""
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size
