#!/usr/bin/python3

"""returns a set of common elements in two sets"""


def common_elements(set_1, set_2):
    result = []

    for i in set_1:
        if i in set_2:
            result.append(i)
    return result
