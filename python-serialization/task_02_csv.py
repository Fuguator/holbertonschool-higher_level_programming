#!/usr/bin/env python3
"""Converting CSV Data to JSON Format"""
import csv
import json


def convert_csv_to_json(filename):
    try:
        with open(filename, 'r') as file:
            csv_read = csv.DictReader(file)
            data = [row for row in csv_read]
            
        with open('data.json', 'w') as jsonfile:
            json.dump(data, jsonfile)
        return True
    except FileNotFoundError as x:
        print(f"Error: {x}")
        return False
