#!/usr/bin/python3

"""define the class square"""


class Square:
    """represent the square"""

    def __init__(self, size=0):

        """initializing the new square.

        Args:
            size(int): the size of the new square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
