#!/usr/bin/python3
"""declare the class"""


class BaseGeometry:
    """the class of the BaseGeometry"""
    def area(self):
        """it raise an exception withe the message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """the validates of the value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
