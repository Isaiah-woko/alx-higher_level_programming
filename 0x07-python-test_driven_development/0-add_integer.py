#!/usr/bin/python3
"""This module contains a function that does addition.
   Args:
       a (int): the first operand of the operation.
       b (int): the second operand of the operation.
"""


def add_integer(a, b=98):
    """This function handles addition of numbers
        Returns: the sum of the addition
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a)) + (int(b))
