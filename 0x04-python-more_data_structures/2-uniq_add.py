#!/usr/bin/python3
"""adds all unique integer in a list """


def uniq_add(my_list=[]):
    result = set(my_list)
    num = 0
    for i in result:
        num += i
    return num
