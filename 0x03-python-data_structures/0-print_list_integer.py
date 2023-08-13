#!/usr/bin/python3
"""ptint all integers of the list
"""

def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
