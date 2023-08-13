#!/usr/bin/python3
"""prints a matrix of intergers"""


def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for column in rows:
            print("{:d}".format(column), end=" " if column != rows[-1] else "")
        print()
