#!/usr/bin/python3
"""inherits the class of the BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle inherit from the basegeometry"""
    def __init__(self, width, height):
        """the width and the height must be the private"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
