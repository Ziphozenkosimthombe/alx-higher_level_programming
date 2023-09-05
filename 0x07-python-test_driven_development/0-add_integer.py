#!/usr/bin/python3
"""declare the function"""


def add_integer(a, b=98):
    """adding the two integers.
    Arg:
        a(int):add the new integer to the function.
        b(int):add tthe new integer to the function.
    Raise:
        TypeError:a and b must be an integer.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    add = int(a) + int(b)
    return add

