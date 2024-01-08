#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for elements in row:
            print("{}".format(elements), end=' ')
        print()
