#!/usr/bin/python3
"""This module contains a class with no class or object attribute"""


class LockedClass(object):
    """This class is locked and has no obj or class attributes
        and has some restriction on creating new instances
    """

    __slots__ = ("first_name")

    def __init__(self, first_name=None):
        self.first_name = first_name
