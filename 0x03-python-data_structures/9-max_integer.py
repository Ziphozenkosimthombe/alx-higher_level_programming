#!/usr/bin/python3

"""function that finds the biggest integer of list"""


def max_integer(my_list=[]):
    if my_list == 0:
        return None
    greater = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > greater:
            greater = my_list[i]
    return greater
