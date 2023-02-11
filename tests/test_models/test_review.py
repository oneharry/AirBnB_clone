#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    def test_no_args_instantiation(self):
        r1 = Review()
        self.assertIsInstance(r1, Review)

    def test_Review_inherits_from_BaseModel(self):
        self.assertTrue(issubclass(Review, BaseModel))
