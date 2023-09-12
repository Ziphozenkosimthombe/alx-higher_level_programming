#!/usr/bin/python3
"""defining the function of Pscal's triangle of n"""


def pascal_triangle(n):
    """Check if n is a valid input"""
    if n <= 0:
        return []
    """Initialize the triangle with the first row"""
    triangle = [[1]]
    """ Loop from the second row to the n row"""
    for a in range(1, n):
        """Initialize the current row with the first element as 1"""
        row = [1]
        """ Loop from the second element to the second last element"""
        for b in range(1, a):
            """Calculate the current element as the sum of
            the two elements above it"""
            row.append(triangle[a-1][b-1] + triangle[a-1][b])
        row.append(1)
        triangle.append(row)
    return triangle
