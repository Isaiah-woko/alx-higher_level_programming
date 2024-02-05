#!/usr/bin/python3

"""This module is an empty class"""


class BaseGeometry:
    """This class object respresnets the definition for the BaseGeometry class
        It has several methods thats defines the Area and some other properties
        of the BaseGeometry class object.
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

        if not isinstance(name, str):
            raise TypeError("{} must be a string".format(name))
