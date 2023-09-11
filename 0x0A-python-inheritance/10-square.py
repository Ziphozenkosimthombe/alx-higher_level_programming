#!/usr/bin/python3
"""declare the inherits from Rectangel"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """initialazing the square"""
    def __init__(self, size):
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size
