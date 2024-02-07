#!/usr/bin/python3

"""This module contains a function for adding attribute"""


def add_attribute(obj, attribute_name, attribute_value):

    if not attribute_name or not attribute_value:
        raise TypeError("can't add new attribute")
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attribute_name, attribute_value)
