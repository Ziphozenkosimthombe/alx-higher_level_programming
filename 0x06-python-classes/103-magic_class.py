#!/usr/bin/python3


"""define a magiclass matching exactly"""

import math


class MagicClass:
    """represent a circle"""

    def __init__(self, radius=0):
        """initialazing a magic class.
        Args:
            radius(float or int): radius of the new magicClass"""

        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        return 2 * math.pi * self.__radius
