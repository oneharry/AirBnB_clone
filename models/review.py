#!/usr/bin/python3
"""This module contans a class 'Review'"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This is a Review Class"""
    place_id = ""
    user_id = ""
    text = ""
