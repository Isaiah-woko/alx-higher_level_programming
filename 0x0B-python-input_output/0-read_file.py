#!/usr/bin/python3

"""This module contains the code for file input"""


def read_file(filename=""):
    """
        This is a function for opening a file using with
        Args:
        filename: The file to open
    """
    with open(filename, "r") as read_data:
        for line in read_data:
            print("{}".format(line), end="")
