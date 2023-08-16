#!/usr/bin/python3

"""returns the weighted average of all integers tuple (<score>, <weight>)"""


def weight_average(my_list=[]):
    if not my_list:
        return 0
    number = 0
    weight = 0

    for i in my_list:
        number += i[0] * i[1]
        weight += i[1]

    return (number/weight)
