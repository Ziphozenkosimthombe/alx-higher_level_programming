#!/usr/bin/python3

"""print all the intergers of all list, in reverse order"""


def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{-1:0}".format(my_list[i]))
