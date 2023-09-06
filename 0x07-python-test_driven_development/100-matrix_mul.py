#!/usr/bin/python3
"""declare the function."""


def matrix_mul(m_a, m_b):
    """initialazing the multiply two matrices.

    Args:
        m_a(ints/floats): The new  first matrix.
        m_b(ints/floats): The new  second matrix.
    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        ValueError: If m_a and m_b cannot be multiplied.
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(rows, list) for rows in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(rows, list) for rows in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(lee, int) or isinstance(lee, float))
               for lee in [number for rows in m_a for number in rows]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(lee, int) or isinstance(lee, float))
               for lee in [number for rows in m_b for number in rows]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(rows) == len(m_a[0]) for rows in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(rows) == len(m_b[0]) for rows in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted = []
    for k in range(len(m_b[0])):
        new_rows = []
        for a in range(len(m_b)):
            new_rows.append(m_b[a][k])
        inverted.append(new_rows)

    new_matrix = []
    for rows in m_a:
        new_rows = []
        for column in inverted:
            product = 0
            for j in range(len(inverted[0])):
                product += rows[j] * column[j]
            new_rows.append(product)
        new_matrix.append(new_rows)

    return new_matrix
