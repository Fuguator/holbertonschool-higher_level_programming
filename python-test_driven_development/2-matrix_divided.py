#!/usr/bin/python3
"""divides each element in matrix"""


def matrix_divided(matrix, div):
    """returns a result of division"""

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not all(len(matrix[0]) == len(matrix[i]) for i in range(len(matrix))):
        raise TypeError("Each row of the matrix must have the same size")
    new_matrix = []
    a = "matrix must be a matrix (list of lists) of integers/floats"
    for row in matrix:
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(a)
            element = round(float(element) / div, 2)
            new_row.append(element)
        new_matrix.append(new_row)
    return new_matrix
