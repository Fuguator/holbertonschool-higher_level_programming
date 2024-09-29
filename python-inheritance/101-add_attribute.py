#!/usr/bin/python3
"""Add attribute"""


def func(obj, name, value):
    """Add attribute"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    return setattr(obj, name, value)
