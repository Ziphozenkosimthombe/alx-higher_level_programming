#!/usr/bin/python3

"""defining the function """


def inherits_from(obj, a_class):
    """return true if the object is an instance of a class that inherited,
    from the specified class, otherwise flase."""
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
