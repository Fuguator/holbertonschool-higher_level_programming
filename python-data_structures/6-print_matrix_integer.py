#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j, k in enumerate(i):
                print("{:d}".format(k), end=" ")
        print()
