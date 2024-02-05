#!/usr/bin/python3

"""This module is an empty class"""


class BaseGeometry:
    """This class object respresnets the definition for the BaseGeometry class
        It has several methods thats defines the Area and some other properties
        of the BaseGeometry class object.
    """

    def area(self):
        raise Exception("area() is not implemented")
