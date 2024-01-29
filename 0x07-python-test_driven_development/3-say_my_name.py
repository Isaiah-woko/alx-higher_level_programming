#!/usr/bin/python3

"""This module contains function for printing out a name
    Args:
    first_name: This is the first name to print
    last_name: This is the last name to print
"""


def say_my_name(first_name, last_name=""):
    """This function handles the printing of first nd last name of user"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("my name is {} {}".format(first_name, last_name))
