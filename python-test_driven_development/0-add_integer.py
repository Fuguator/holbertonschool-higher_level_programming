#!/usr/bin/python3
"""returns a sum"""


def add_integer(a, b=98):
    """takes a sum of a and b"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a + b)
