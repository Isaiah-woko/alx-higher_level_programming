#!/usr/bin/python3
"""This module contains a function that divides a matrix
    Args:
    matrix: the matrix to divide
    div: the number to divide the matrix by
"""


def matrix_divided(matrix, div):
    """This function handles the division of the matrix
        Returns: the new divided matrix
    """

    new_matrix = [[]]

    err_msg = "matrix must be a matrix (list of lists) of integers/floats"

    # handling matrix edge cases
    for rows in matrix:
        if not isinstance(rows, list):
            raise TypeError(err_msg)

    for elements in rows:
        if not isinstance(elements, (int, float)):
            raise TypeError(err_msg)

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    # handling div edge cases
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    new_matrix = [[round((i / div), 2)for i in rows]for rows in matrix]

    return new_matrix
