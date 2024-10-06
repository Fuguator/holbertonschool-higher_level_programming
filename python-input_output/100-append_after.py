#!/usr/bin/python3
"""Search and update"""


def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for i in lines:
            if search_string in i:
                file.write(new_string)
            file.write(i)
