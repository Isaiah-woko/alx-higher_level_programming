#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for row in matrix:
        for index, elements in enumerate(row):
            if index == len(row) - 1:
                print("{}".format(elements), end='')
            else:
                print("{}".format(elements), end=' ')
        print()
