#!/usr/bin/python3

"""This module contains a function for adding attribute"""


def add_attribute(obj, attribute_name, attribute_value):

    """
    This function dynamically adds a new attribute

    Args:
        obj: this is an object of the class for the new attribute.
        Attribute_name: the attribute name
        Attribute_value: the attribute value
    """

    if not attribute_name or not attribute_value:
        raise TypeError("can't add new attribute")
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attribute_name, attribute_value)
