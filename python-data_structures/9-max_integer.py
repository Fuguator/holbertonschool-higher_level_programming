#!/usr/bin/python3
def max_integer(my_list=[]):
    max_value = 0
    for i in my_list:
        if my_list[i] > max_value:
            max_value = my_list[i]
    return max_value