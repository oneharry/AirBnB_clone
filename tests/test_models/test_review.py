#!/usr/bin/python3
""" Test Module for class Review """
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """ Test Class definition for class Review """
    def test_no_args_instantiation(self):
        """ Tests for instance of the class object """
        r1 = Review()
        self.assertIsInstance(r1, Review)

    def test_Review_inherits_from_BaseModel(self):
        """ Tests if the class Review inherited class BaseModel """
        self.assertTrue(issubclass(Review, BaseModel))


if __name__ == "__main__":
    unittest.main()
