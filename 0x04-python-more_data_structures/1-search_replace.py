#!/usr/bin/python3

"""function that replaces all accurrences of an element by another in a new list"""


def search_replace(my_list, search, replace):
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return new_list
