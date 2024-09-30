#!/usr/bin/python3
"""read file"""


def read_file(filename=""):
    """read file"""
    with open(filename, "r", encoding='utf-8') as e:
        print(e.read(), end='')
