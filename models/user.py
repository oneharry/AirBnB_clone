#!/usr/bin/python3
"""This module contans a class 'User'"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class creates a User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
