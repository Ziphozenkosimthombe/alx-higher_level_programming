#!/usr/bin/python3
"""define the function that adds attributes to an object"""


def add_attribute(obj, attribute, value):
    """the new attribute to be added to an object"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
