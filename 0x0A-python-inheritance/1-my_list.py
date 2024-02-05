#!/usr/bin/python3

"""This module inherits a class and works on it"""


class MyList(list):

    """This function is a subclass of the list class
        and it prints the list but in a sorted manner
    """

    def print_sorted(self):
        print(sorted(self))
