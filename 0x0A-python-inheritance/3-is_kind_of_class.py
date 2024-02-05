#!/usr/bin/python3

"""This module contains a function for returning anm instance"""


def is_kind_of_class(obj, a_class):
    """ This function returns True if the object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class
    """

    return isinstance(obj, a_class)
