#!/usr/bin/python3
"""inherit from"""


def inherits_from(obj, a_class):
    """inherit from"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
