#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_no_args_instantiation(self):
        a1 = Amenity()
        self.assertIsInstance(a1, Amenity)

    def test_Amenity_inherits_from_BaseModel(self):
        self.assertTrue(issubclass(Amenity, BaseModel))
