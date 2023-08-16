#!/usr/bin/python3
"""returns a new dictionary with all values multiplied by 2"""


def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    for key in new_dictionary:
        new_dictionary[key] *= 2
    return new_dictionary
