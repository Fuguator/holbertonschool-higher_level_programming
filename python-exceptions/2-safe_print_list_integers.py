#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    length = 0
    try:
        for i in range(0, x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end='')
                length += 1
        print()
        return length
    except (TypeError, ValueError):
        print()
