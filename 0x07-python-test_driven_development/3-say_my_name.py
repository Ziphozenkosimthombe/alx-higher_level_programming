#!/usr/bin/python3
"""declare the function"""


def say_my_name(first_name, last_name=""):
    """initialazing the new first name and last name.
    Arg:
        first_name and last_name(str): must be an string
    Raise:
        TypeError:first_name must be a string or last_name must be a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
