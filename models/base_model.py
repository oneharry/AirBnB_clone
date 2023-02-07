#!/usr/bin/python3
""" Module define a base class BaseModel """
import uuid
from datetime import datetime


class BaseModel:
    """ class BaseModel: This is a base class for creating new instances """
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
