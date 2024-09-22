#!/usr/bin/python3
"""function that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """conditionsssssss"""
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if not all(isinstance(item, list) for item in m_a):
        raise TypeError('m_a must be a list of lists')
    if not all(isinstance(item, list) for item in m_b):
        raise TypeError('m_b must be a list of lists')
    if not any(m_a):
        raise ValueError("m_a can't be empty")
    if not any(m_b):
        raise ValueError("m_b can't be empty")
    if not all(isinstance(i, float) or isinstance(i, int)
               for j in m_a for i in j):
        raise TypeError('m_a should contain only integers or floats')
    if not all(isinstance(i, float) or isinstance(i, int)
               for j in m_b for i in j):
        raise TypeError('m_b should contain only integers or floats')
    if not all(len(i) == len(m_a[0]) for i in m_a):
        raise TypeError('each row of m_a must be of the same size')
    if not all(len(i) == len(m_b[0]) for i in m_b):
        raise TypeError('each row of m_b must be of the same size')
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return [[
        sum(a * b for a, b in zip(a_row, b_col))
        for b_col in zip(*m_b)]
            for a_row in m_a]
