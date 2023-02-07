#!/usr/bin/python3
"""This module contains a class `BaseModel`"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """This class defines all common attributes/methods for other classes
    """
    def __init__(self):
        """Creates an instance"""
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns a printable representation of a BaseModel instance."""
        st = "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
        return st

    def save(self):
        """
        Method updates the attr -updated_at- with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
            returns the dictionary represntation of the object
        """
        dic = self.__dict__
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic