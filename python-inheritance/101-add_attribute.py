#!/usr/bin/python3
"""add_attribute"""


def add_attribute(obj, name: str, val: str):
    """add_attribute"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    return setattr(obj, name, val)