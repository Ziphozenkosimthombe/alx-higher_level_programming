#!/usr/bin/python3
"""declare the function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """the multiplication of two matrices.

    Args:
        m_a(ints/floats): The new first matrix.
        m_b(ints/floats): The new second matrix.
    """

    return (np.matmul(m_a, m_b))
