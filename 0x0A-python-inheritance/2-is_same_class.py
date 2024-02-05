#!/usr/bin/python3

"""This module has a function for checking instances"""


def is_same_class(obj, a_class):

    """This function returns True if the object is
        exactly an instance of the specified class ; otherwise False.
    """

    return type(obj) is a_class
