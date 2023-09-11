#!/usr/bin/python3
"""defining the function"""


def is_same_class(obj, a_class):
    """return true if the object is exactly an instance of specified class,
    otherwise false."""

    obj_1 = type(obj)

    if obj_1 == a_class:
        return True
    return False
