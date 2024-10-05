#!/usr/bin/env python3
"""Converting CSV Data to JSON Format"""
import csv
import json


def convert_csv_to_json(csvFilePath, jsonFilePath):

    data = {}

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            key = rows['No']
            data[key] = rows

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
