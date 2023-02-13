#!/usr/bin/python3
""" Test Module for testing class City """
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """ Class Test definition for class City """
    def test_no_args_instantiation(self):
        """ Tests for the instance of class object """
        c1 = City()
        self.assertIsInstance(c1, City)

    def test_City_inherits_from_BaseModel(self):
        """ tests if the class City inherited the class BaseModel """
        self.assertTrue(issubclass(City, BaseModel))


if __name__ == "__main__":
    unittest.main()
