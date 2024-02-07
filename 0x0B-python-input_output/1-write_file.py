#!/usr/bin/python3

"""This module contains the code for file input"""


def write_file(filename="", text=""):
    """
        This is a function for writing text to a file using with
        Args:
        filename: The file to open
        text: the text to write on the file
    """

    with open(filename, "w") as write_file:
        write_file.write(text)

    return len(text)
