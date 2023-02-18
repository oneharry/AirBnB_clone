#!/usr/bin/python3
""" Test Module for class City """
import unittest
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """ Test City definition"""
    def test_no_args_instantiation(self):
        """ test for instance of object """
        ct = City()
        self.assertIsInstance(ct, City)

    def test_City_inherits_from_BaseModel(self):
        """ Tests if class City inherited class BaseModel """
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        """ Validates that City has necessary attributes"""
        ct = City()

        self.assertTrue(hasattr(ct, "name"))
        self.assertTrue(hasattr(ct, "state_id"))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), storage.all().values())

    def test_attribute_types(self):
        """Validates attribute types"""
        ct = City()

        self.assertEqual(str, type(ct.id))
        self.assertEqual(datetime, type(ct.created_at))
        self.assertEqual(datetime, type(ct.updated_at))
        self.assertEqual(str, type(ct.name))
        self.assertEqual(str, type(ct.state_id))


if __name__ == "__main__":
    unittest.main()
