#!/usr/bin/python3
"""load_from_json_file"""
import json


def load_from_json_file(filename):
    """load_from_json_file"""
    with open(filename, 'r') as file:
        my_obj = json.loads(file.read())
        return my_obj
