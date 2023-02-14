#!/usr/bin/python3
""" Terv Module for class Review """
import unittest
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """ Test Review definition"""
    def test_no_args_instantiation(self):
        """ test for instance of object """
        rv = Review()
        self.assertIsInstance(rv, Review)

    def test_Review_inherits_from_BaseModel(self):
        """ Tests if class Review inherited  from class BaseModel """
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attributes(self):
        """ Validates that Review has necessary attributes"""
        rv = Review()

        self.assertTrue(hasattr(rv, "text"))
        self.assertTrue(hasattr(rv, "place_id"))
        self.assertTrue(hasattr(rv, "user_id"))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), storage.all().values())

    def test_attribute_types(self):
        """Validates attribute types"""
        rv = Review()

        self.assertEqual(str, type(rv.id))
        self.assertEqual(datetime, type(rv.created_at))
        self.assertEqual(datetime, type(rv.updated_at))
        self.assertEqual(str, type(rv.text))
        self.assertEqual(str, type(rv.place_id))
        self.assertEqual(str, type(rv.user_id))


if __name__ == "__main__":
    unittest.main()
