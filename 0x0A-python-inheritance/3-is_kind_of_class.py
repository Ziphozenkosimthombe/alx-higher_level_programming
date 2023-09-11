#!/usr/bin/python3

"""defining the function check the instance"""


def is_kind_of_class(obj, a_class):
    """return true if the object is an insatance of, or if the objectis,
    an instance of a class that inherited from, the specified class,
    otherwise return false."""

    return isinstance(obj, a_class)
