#!/usr/bin/python3
"""returns a sum"""
def add_integer(a, b=98):
    """takes a sum of a and b"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a + b)
