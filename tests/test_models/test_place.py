#!/usr/bin/python3
""" Test Module for class Place """
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Test Place definition"""
    def test_no_args_instantiation(self):
        """ test for instance of object """
        p1 = Place()
        self.assertIsInstance(p1, Place)

    def test_Place_inherits_from_BaseModel(self):
        """ Tests if class Place inherited class BaseModel """
        self.assertTrue(issubclass(Place, BaseModel))


if __name__ == "__main__":
    unittest.main()
