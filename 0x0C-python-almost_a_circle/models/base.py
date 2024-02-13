#!/usr/bin/python3

"""This module contains a class defintion of the Base models class"""


import json


class Base(object):
    """This is the class defition of the base model.

       Attributes:
           id: this represents the id of the class.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save objects to a JSON file."""
        filename = f"{cls.__name__}.json"
        json_objs = [obj.to_dictionary() for obj in list_objs]

        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                file.write(cls.to_json_string(json_objs))
