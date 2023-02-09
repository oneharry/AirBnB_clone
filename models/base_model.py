#!/usr/bin/python3
"""This module contains a class `BaseModel`"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """This class defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """Creates an instance"""
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.now()
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "created_at" or k == "updated_at":
                        self.__dict__[k] = datetime.fromisoformat(v)
                    else:
                        self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """Returns a printable representation of a BaseModel instance."""
        st = "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
        return st

    def save(self):
        """
        Method updates the attr -updated_at- with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            returns the dictionary represntation of the object
        """
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic
