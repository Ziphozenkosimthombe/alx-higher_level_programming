#!/usr/bin/python3
"""declare the class inherits"""


class MyList(list):
    """the class with the inherits of the list"""

    def print_sorted(self):
        """function will print the list, sorted"""
        print(sorted(self))
