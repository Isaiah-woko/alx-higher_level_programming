#!/usr/bin/python3

"""This is a module for json representation"""

import json


def save_to_json_file(my_obj, filename):

    """This function writes an Object to a
        text file, using a JSON representation:

        Args:
        my_str: The object to return JSON representation
        filename: the file to write to
    """

    with open(filename, "w") as write_file:
        write_file.write(json.dumps(my_obj))
