#!/usr/bin/python3
"""write_file"""


def write_file(filename="", text=""):
    """write_file"""
    with open(filename, "a+", encoding='utf-8') as file:
        return file.write(text)
