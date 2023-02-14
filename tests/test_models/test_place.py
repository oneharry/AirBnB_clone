#!/usr/bin/python3
""" Test Module for class Place """
import unittest
from models import storage
from datetime import datetime
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

    def test_attributes(self):
        """ Validates that Place has necessary attributes"""
        pl = Place()

        self.assertTrue(hasattr(pl, "name"))
        self.assertTrue(hasattr(pl, "city_id"))
        self.assertTrue(hasattr(pl, "user_id"))
        self.assertTrue(hasattr(pl, "description"))
        self.assertTrue(hasattr(pl, "number_rooms"))
        self.assertTrue(hasattr(pl, "number_bathrooms"))
        self.assertTrue(hasattr(pl, "max_guest"))
        self.assertTrue(hasattr(pl, "price_by_night"))
        self.assertTrue(hasattr(pl, "latitude"))
        self.assertTrue(hasattr(pl, "longitude"))
        self.assertTrue(hasattr(pl, "amenity_ids"))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), storage.all().values())

    def test_attribute_types(self):
        """Validates attribute types"""
        pl = Place()

        self.assertEqual(str, type(pl.id))
        self.assertEqual(datetime, type(pl.created_at))
        self.assertEqual(datetime, type(pl.updated_at))
        self.assertEqual(str, type(pl.name))
        self.assertEqual(str, type(pl.city_id))
        self.assertEqual(str, type(pl.user_id))
        self.assertEqual(str, type(pl.description))
        self.assertEqual(int, type(pl.number_rooms))
        self.assertEqual(int, type(pl.number_bathrooms))
        self.assertEqual(int, type(pl.max_guest))
        self.assertEqual(int, type(pl.price_by_night))
        self.assertEqual(float, type(pl.latitude))
        self.assertEqual(float, type(pl.longitude))
        self.assertEqual(list, type(pl.amenity_ids))


if __name__ == "__main__":
    unittest.main()
