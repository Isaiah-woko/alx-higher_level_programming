#!/usr/bin/python3

"""This module contains the code for file input"""


def read_file(filename=""):
    """
        This is a function for opening a file using with
        Args:
        filename: The file to open
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print("{}".format(read_data))
