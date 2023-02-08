#!/usr/bin/python3
"""This module contains the class `FileStorage`"""
import json


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj_id = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[obj_id] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        newdict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as newfile:
            json.dump(newdict, newfile)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists; otherwise, nothing is done.
        If the file doesn’t exist, no exception is  raised)
        """
        try:
            with open(FileStorage.__file_path) as readfile:
               FileStorage.__objects = json.load(readfile)
        except FileNotFoundError:
            return
