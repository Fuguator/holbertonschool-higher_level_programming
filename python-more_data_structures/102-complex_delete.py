#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_list = []
    for i, dict_val in a_dictionary.items():
        if value is dict_val:
            new_list.append(i)
    if len(new_list) > 0:
        for new in new_list:
            del a_dictionary[new]
    return a_dictionary
