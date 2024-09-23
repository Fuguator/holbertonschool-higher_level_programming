#!/usr/bin/python3
"""class MyList"""


class MyList(list):
    """sorts list"""
    def print_sorted(self):
        print(sorted(self))
