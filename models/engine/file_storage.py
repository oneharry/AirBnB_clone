#!/usr/bin/python3
"""This module contains the class `FileStorage`"""
import json
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        """
        sets in __objects the obj with key <obj class name>.id
        """
        obj_id = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[obj_id] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        newdict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as newfile:
            json.dump(newdict, newfile)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists; otherwise, nothing is done
        If the file doesn’t exist, no exception is  raised)
        """
        objects = {}
        try:
            with open(FileStorage.__file_path) as readfile:
                objects = json.load(readfile)
                for k, obj_dict in objects.items():
                    clsname = obj_dict.pop("__class__")
                    obj = getattr(sys.modules[__name__], clsname)
                    self.new(obj(**obj_dict))
        except FileNotFoundError:
            return
