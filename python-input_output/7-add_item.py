#!/usr/bin/python3
"""adds all arguments to a Python list"""
from sys import argv


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def main():
    """adds all arguments to a Python list"""

    try:
        my_obj = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_obj = []
    my_obj += argv[1:]
    save_to_json_file(my_obj, "add_item.json")

if __name__ == "__main__":
    main()
