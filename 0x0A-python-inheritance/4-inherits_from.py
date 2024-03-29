#!/usr/bin/python3

"""This modue contains the class for return instances"""


def inherits_from(obj, a_class):

    """This function returns True if the object is an instance
        of a class that inherited (directly or indirectly) from the
        specified class ; otherwise False.
    """

    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
