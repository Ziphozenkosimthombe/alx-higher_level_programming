#!/usr/bin/python3
"""declare the function"""


def print_square(size):
    """intialazing the new size.
    Arg:
        size(int):the new size of the square.
    Raise:
        TypeError:size must be an integer
        ValueError:size must be >= 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for k in range(size):
        [print('#', end='')for a in range(size)]
        print('')
