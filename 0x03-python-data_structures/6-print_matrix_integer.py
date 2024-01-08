#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for row in matrix:
        for index, elements in enumerate(row):
            if index == len(row) - 1:
                print("{:d}".format(elements), end='')
            else:
                print("{:d}".format(elements), end=' ')
        print()
