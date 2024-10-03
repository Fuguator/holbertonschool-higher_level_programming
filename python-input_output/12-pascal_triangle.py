#!/usr/bin/python3
"""pascal_triangle"""


def pascal_triangle(n, triangle=None):
    if n <= 0:
        return []

    if triangle is None:
        triangle = [[1]]

    if len(triangle) == n:
        return triangle

    last_row = triangle[-1]
    row = [1] + [last_row[j] + last_row[j + 1] for j in range(len(last_row) - 1)] + [1]

    triangle.append(row)

    return pascal_triangle(n, triangle)
