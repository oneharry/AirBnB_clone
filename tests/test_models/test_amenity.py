#!/usr/bin/python3
""" Test Module for class Amenity """
import unittest
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Test Amenity definition"""
    def test_no_args_instantiation(self):
        """ test for instance of objeam """
        am = Amenity()
        self.assertIsInstance(am, Amenity)

    def test_Amenity_inherits_from_BaseModel(self):
        """ Tests if class Amenity inherited class BaseModel """
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attributes(self):
        """ Validates that Amenity has necessary attributes"""
        am = Amenity()

        self.assertTrue(hasattr(am, "name"))

    def test_new_instance_stored_in_objeams(self):
        self.assertIn(Amenity(), storage.all().values())

    def test_attribute_types(self):
        """Validates attribute types"""
        am = Amenity()

        self.assertEqual(str, type(am.id))
        self.assertEqual(datetime, type(am.created_at))
        self.assertEqual(datetime, type(am.updated_at))
        self.assertEqual(str, type(am.name))


if __name__ == "__main__":
    unittest.main()
