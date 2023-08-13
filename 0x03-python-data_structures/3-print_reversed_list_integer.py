#!/usr/bin/python3

"""print all the intergers of all list, in reverse order"""


def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
