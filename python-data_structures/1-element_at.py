#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 and idx + 1 > len(my_list):
        return None
    else:
        print("Element at index {:d} is {}".format(idx, my_list[idx]))
