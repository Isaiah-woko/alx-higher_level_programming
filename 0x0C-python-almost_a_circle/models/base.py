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
        """this method saves to file"""
        cls.json_obj_list = []
        cls.filename = "{}.json".format(cls.__name__)

        for cls_obj in list_objs:
            cls.json_obj_list.append(cls_obj.to_dictionary())

        with open(cls.filename, "w") as file:
            file.write(cls.to_json_string(cls.json_obj_list))

    @staticmethod
    def from_json_string(json_string):
        """converts from json"""
        if json_string is None:
            return []
        else:
            return json_string

    @classmethod
    def create(cls, **dictionary):
        """creates a new instance"""
        if cls.__name__ == "Rectangle":
            instance = cls(5, 10)
        elif cls.__name__ == "Square":
            instance = cls(7)
        else:
            raise TypeError("unknow")
        instance.update(**dictionary)

        return instance
