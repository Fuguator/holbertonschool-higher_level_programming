#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j, k in enumerate(i):
            if j < len(i) - 1:
                print("{:d}".format(k), end=" ")
            else:
                print("{:d}".format(k), end="")
        print()
