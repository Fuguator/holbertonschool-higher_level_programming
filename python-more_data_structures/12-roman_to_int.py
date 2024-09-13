#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or isinstance(roman_string, str):
        return None
    values, sum = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}, 0
    for i in range(len(roman_string)):
        if i > 0 and values[roman_string[i]] > values[roman_string[i - 1]]:
            sum += values[roman_string[i]] - (values[roman_string[i - 1]] * 2)
        else:
            sum += values[roman_string[i]]
    return sum
