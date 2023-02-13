#!/usr/bin/python3
""" Test Module for class Amenity """
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Test Class definition """
    def test_no_args_instantiation(self):
        """ Test for an instance of class Amenity """
        a1 = Amenity()
        self.assertIsInstance(a1, Amenity)

    def test_Amenity_inherits_from_BaseModel(self):
        """ Tests if Amenity class inherited the class BaseModel """
        self.assertTrue(issubclass(Amenity, BaseModel))


if __name__ == "__main__":
    unittest.main()
