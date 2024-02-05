#!/usr/bin/python3

"""This module is for the function that returns attributes"""


class list:

    """This class returns a list of all
            the objects attributs and methods
        """

    def lookup(obj):

        """The function for returning the obj attributes"""
        return dir(obj)
