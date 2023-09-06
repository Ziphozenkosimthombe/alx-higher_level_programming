#!/usr/bin/python3
"""declare the function of matrix"""


def matrix_divided(matrix, div):
    """initializing the new matrix of the list of integers or float.
    Arg:
        matrix(int or float): new values of matrix
        div(int or float):new values of divi
    Raise:
        TypeError:matrix must be a matrix of integers/floats and
        Each row of the matrix must have the same size.
        TypeError:div must be a number
        ZeroDivisionError:division by zero
    """
    if (
        not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(rows, list) for rows in matrix) or
        not all((isinstance(lee, int) or isinstance(lee, float))
                for lee in [number for rows in matrix for number in rows])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(rows) == len(matrix[0]) for rows in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), rows)) for rows in matrix])
