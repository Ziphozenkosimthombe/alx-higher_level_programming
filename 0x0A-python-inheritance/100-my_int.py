#!/usr/bin/python3
"""declare the class that inherits from int"""


class MyInt(int):
    """initializing the the class of MyInt"""

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
