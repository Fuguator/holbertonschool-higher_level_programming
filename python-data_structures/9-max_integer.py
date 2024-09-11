#!/usr/bin/python3
def max_integer(my_list=[]):
    max_value = 0
    for i in len(my_list):
        if my_list[i] > max_value:
            max_value = my_list[i]
        else:
            continue          
    return max_value
