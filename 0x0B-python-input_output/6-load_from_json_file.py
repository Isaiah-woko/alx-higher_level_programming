#!/usr/bin/python3

"""This is a module for json representation"""

import json


def load_from_json_file(filename):

    """This function writes an Object to a
        text file, using a JSON representation:

        Args:
        filename: the file to read from
    """

    with open(filename, "r") as read_file:
        data = json.load(read_file)

    return data
